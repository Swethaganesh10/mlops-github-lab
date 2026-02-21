def fun1(data):
    """
    Calculates the mean of a list of numbers.
    Args:
        data (list): A list of int/float values.
    Returns:
        float: Mean of the data.
    Raises:
        ValueError: If data is empty or contains non-numeric values.
    """
    if not data:
        raise ValueError("Data list cannot be empty.")
    if not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("All elements must be numeric.")
    return sum(data) / len(data)


def fun2(data):
    """
    Calculates the median of a list of numbers.
    Args:
        data (list): A list of int/float values.
    Returns:
        float: Median of the data.
    Raises:
        ValueError: If data is empty or contains non-numeric values.
    """
    if not data:
        raise ValueError("Data list cannot be empty.")
    if not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("All elements must be numeric.")
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    return float(sorted_data[mid])


def fun3(data):
    """
    Calculates the standard deviation of a list of numbers.
    Args:
        data (list): A list of int/float values.
    Returns:
        float: Standard deviation of the data.
    Raises:
        ValueError: If data has fewer than 2 elements.
    """
    if len(data) < 2:
        raise ValueError("Data must have at least 2 elements.")
    mean = fun1(data)
    variance = sum((x - mean) ** 2 for x in data) / (len(data) - 1)
    return variance ** 0.5


def fun4(data):
    """
    Returns a summary dict with mean, median, and standard deviation.
    Args:
        data (list): A list of int/float values.
    Returns:
        dict: Summary statistics (mean, median, std_dev).
    """
    return {
        "mean": fun1(data),
        "median": fun2(data),
        "std_dev": fun3(data)
    }