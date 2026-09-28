"""Every request model must be importable from ``wsapi_client.models``."""

import importlib
import pkgutil

import wsapi_client.models as models
import wsapi_client.models.requests as requests_pkg


def _request_classes():
    """Yield (module, name, class) for every class defined under models.requests."""
    for info in pkgutil.walk_packages(requests_pkg.__path__, requests_pkg.__name__ + "."):
        module = importlib.import_module(info.name)
        for name, obj in vars(module).items():
            if isinstance(obj, type) and obj.__module__ == module.__name__:
                yield module.__name__, name, obj


def test_every_request_model_has_a_short_import():
    missing = [f"{mod}.{name}" for mod, name, _ in _request_classes() if not hasattr(models, name)]
    assert not missing, f"not re-exported from wsapi_client.models: {missing}"


def test_short_import_is_the_same_class_as_the_long_one():
    for mod, name, obj in _request_classes():
        assert getattr(models, name) is obj, f"{mod}.{name}"


def test_documented_imports_still_work():
    from wsapi_client.models import BulkCheckRequest, MessageSendTextRequest, SendMediaRequest
    from wsapi_client.models.requests.messages import MessageSendTextRequest as LongText

    assert MessageSendTextRequest is LongText
    assert SendMediaRequest and BulkCheckRequest
