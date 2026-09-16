from datetime import datetime, timezone

from dsbench.metrics import is_peak, nominal_cost, conservative_request_cost

PRICING = {
    "currency": "USD",
    "weekday_peak_windows_utc": ["01:00-04:00", "06:00-10:00"],
    "offpeak": {"input_miss": 0.15, "input_cache": 0.003, "output": 0.60},
    "peak": {"input_miss": 0.30, "input_cache": 0.006, "output": 1.20},
}


def test_peak_window_weekday_and_weekend():
    assert is_peak(PRICING, datetime(2026, 9, 16, 2, 0, tzinfo=timezone.utc))
    assert not is_peak(PRICING, datetime(2026, 9, 16, 5, 0, tzinfo=timezone.utc))
    assert not is_peak(PRICING, datetime(2026, 9, 19, 2, 0, tzinfo=timezone.utc))


def test_nominal_cost_separates_cached_tokens():
    usage = {"input_tokens": 1000, "cached_input_tokens": 400, "output_tokens": 500}
    result = nominal_cost(PRICING, usage, datetime(2026, 9, 16, 2, 0, tzinfo=timezone.utc))
    expected = (600 * 0.30 + 400 * 0.006 + 500 * 1.20) / 1_000_000
    assert result["price_window"] == "peak"
    assert abs(result["nominal_cost"] - expected) < 1e-12


def test_conservative_guard_uses_peak_rates():
    cost = conservative_request_cost(PRICING, input_bytes=3000, max_output_tokens=1000, when=datetime(2026, 9, 16, 2, 0, tzinfo=timezone.utc))
    assert cost is not None
    assert cost > 0
