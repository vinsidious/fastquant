# Import from package
from fastquant.strategies import (
    RSIStrategy,
    SMACStrategy,
    BaseStrategy,
    DFMAStrategy,
    MACDStrategy,
    EMACStrategy,
    BBandsStrategy,
    BuyAndHoldStrategy,
    SentimentStrategy,
    CustomStrategy,
    TernaryStrategy,
)

# Register your strategy here
STRATEGY_MAPPING = {
    "dfma": DFMAStrategy,
    "rsi": RSIStrategy,
    "smac": SMACStrategy,
    "base": BaseStrategy,
    "macd": MACDStrategy,
    "emac": EMACStrategy,
    "bbands": BBandsStrategy,
    "buynhold": BuyAndHoldStrategy,
    "sentiment": SentimentStrategy,
    "custom": CustomStrategy,
    "ternary": TernaryStrategy,
}
