"""絶対湿度計算の単体テスト."""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from humidity import calc_absolute_humidity


def test_20c_50pct() -> None:
    """20℃ / 50%RH → 約 8.65 g/m³."""
    ah = calc_absolute_humidity(20.0, 50.0)
    assert 8.5 <= ah <= 8.8, f"expected ~8.65, got {ah}"


def test_25c_60pct() -> None:
    """25℃ / 60%RH → 約 13.82 g/m³."""
    ah = calc_absolute_humidity(25.0, 60.0)
    assert 13.5 <= ah <= 14.1, f"expected ~13.82, got {ah}"


def test_0c_100pct() -> None:
    """0℃ / 100%RH → 約 4.85 g/m³."""
    ah = calc_absolute_humidity(0.0, 100.0)
    assert 4.7 <= ah <= 5.0, f"expected ~4.85, got {ah}"


def test_30c_80pct() -> None:
    """30℃ / 80%RH → 約 24.27 g/m³."""
    ah = calc_absolute_humidity(30.0, 80.0)
    assert 24.0 <= ah <= 24.6, f"expected ~24.27, got {ah}"
