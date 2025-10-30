import os

import pytest

from fsspeckit.storage_options.cloud import (
    AwsStorageOptions,
    AzureStorageOptions,
    GcsStorageOptions,
)


def test_aws_object_store_conditional_put_variants():
    options = AwsStorageOptions(access_key_id="key", secret_access_key="secret")

    base_kwargs = options.to_object_store_kwargs()
    assert "conditional_put" not in base_kwargs

    bool_kwargs = options.to_object_store_kwargs(with_conditional_put=True)
    assert bool_kwargs["conditional_put"] == "etag"

    explicit_kwargs = options.to_object_store_kwargs(conditional_put="md5")
    assert explicit_kwargs["conditional_put"] == "md5"


def test_aws_to_storage_options_dict_deprecated_warning():
    options = AwsStorageOptions(access_key_id="key", secret_access_key="secret")
    with pytest.warns(DeprecationWarning):
        deprecated = options.to_storage_options_dict()

    assert deprecated["conditional_put"] == "etag"
    assert deprecated["access_key_id"] == "key"


def test_aws_allow_invalid_certs_alias_warns():
    with pytest.warns(DeprecationWarning):
        options = AwsStorageOptions(allow_invalid_certs=True)

    assert options.allow_invalid_certificates is True
    assert options.allow_invalid_certs is None


def test_aws_to_fsspec_kwargs_filters_none_values():
    options = AwsStorageOptions(
        access_key_id="key",
        secret_access_key="secret",
        region="us-east-1",
    )

    kwargs = options.to_fsspec_kwargs()
    assert kwargs["client_kwargs"]["region_name"] == "us-east-1"
    assert "verify" not in kwargs["client_kwargs"]
    assert "use_ssl" not in kwargs["client_kwargs"]

    options = AwsStorageOptions(
        access_key_id="key",
        secret_access_key="secret",
        allow_invalid_certificates=True,
        allow_http=True,
    )
    kwargs = options.to_fsspec_kwargs()
    client_kwargs = kwargs["client_kwargs"]
    assert client_kwargs["verify"] is False
    assert client_kwargs["use_ssl"] is False


def test_aws_to_obstore_kwargs_sanitises_client_options():
    base = AwsStorageOptions()
    base_kwargs = base.to_obstore_kwargs()
    assert "client_options" not in base_kwargs
    assert "default_region" not in base_kwargs

    enriched = AwsStorageOptions(
        allow_invalid_certificates=True,
        allow_http=False,
    )
    merged = enriched.to_obstore_kwargs(client_options={"extra": "value"})
    client_opts = merged["client_options"]
    assert client_opts["allow_invalid_certificates"] is True
    assert client_opts["allow_http"] is False
    assert client_opts["extra"] == "value"


def test_aws_env_roundtrip(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("AWS_ACCESS_KEY_ID", "env-key")
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "env-secret")
    monkeypatch.setenv("AWS_SESSION_TOKEN", "env-token")
    monkeypatch.setenv("AWS_ENDPOINT_URL", "http://localhost:9000")
    monkeypatch.setenv("AWS_DEFAULT_REGION", "us-west-2")
    monkeypatch.setenv("ALLOW_INVALID_CERTIFICATES", "yes")
    monkeypatch.setenv("AWS_ALLOW_HTTP", "1")

    options = AwsStorageOptions.from_env()
    assert options.access_key_id == "env-key"
    assert options.allow_invalid_certificates is True
    assert options.allow_http is True

    for key in [
        "AWS_ACCESS_KEY_ID",
        "AWS_SECRET_ACCESS_KEY",
        "AWS_SESSION_TOKEN",
        "AWS_ENDPOINT_URL",
        "AWS_DEFAULT_REGION",
        "ALLOW_INVALID_CERTIFICATES",
        "AWS_ALLOW_HTTP",
    ]:
        monkeypatch.delenv(key, raising=False)

    options.to_env()
    assert os.getenv("AWS_ACCESS_KEY_ID") == "env-key"
    assert os.getenv("ALLOW_INVALID_CERTIFICATES") == "True"
    assert os.getenv("AWS_ALLOW_HTTP") == "True"


def test_gcs_protocol_normalisation():
    options = GcsStorageOptions(protocol="gcs")
    assert options.protocol == "gs"


def test_azure_protocol_validation_and_kwargs():
    options = AzureStorageOptions(protocol="az", account_name="acct", account_key="key")
    kwargs = options.to_fsspec_kwargs()
    assert kwargs["account_name"] == "acct"
    assert kwargs["account_key"] == "key"

    with pytest.raises(ValueError):
        AzureStorageOptions(protocol="blob")
