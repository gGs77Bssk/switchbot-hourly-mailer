"""絶対湿度の計算 (Tetens の式 + 気体の状態方程式)."""


def calc_absolute_humidity(temperature: float, relative_humidity: float) -> float:
    """室温と相対湿度から絶対湿度 (g/m³) を算出する.

    Args:
        temperature: 気温 (℃)
        relative_humidity: 相対湿度 (%)

    Returns:
        絶対湿度 (g/m³), 小数点以下2桁に丸め
    """
    e_s = 6.1078 * 10 ** ((7.5 * temperature) / (temperature + 237.3))
    e = e_s * relative_humidity / 100
    ah = 217 * e / (temperature + 273.15)
    return round(ah, 2)
