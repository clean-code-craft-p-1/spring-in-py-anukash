import math


def calculateStats(numbers):
  """Calculate average, minimum, and maximum of a list of numbers."""

  if not numbers:
      return {"avg": math.nan, "min": math.nan, "max": math.nan}
  
  return {
      "avg": sum(numbers) / len(numbers),
      "min": min(numbers),
      "max": max(numbers),
  }
