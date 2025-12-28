from src.attributes.datasets_list import DATASETS, available_datasets


def normalize_name(name: str) -> str:
    return name.replace(" ", "").replace("_", "").lower()


def generate(dataset_name: str, rows: int):
    """
    Generate fake dataset rows.
    """
    normalized_name = normalize_name(dataset_name)

    if normalized_name not in DATASETS:
        raise ValueError(
            f"Dataset '{dataset_name}' not found. Available: {available_datasets()}"
        )

    generator_func = DATASETS[normalized_name]

    # Dataset-specific behavior
    if normalized_name == "employeedataset":
        return generator_func(num=rows)

    elif normalized_name == "courier":
        return generator_func(num=rows).couriers()

    elif normalized_name == "retailsales":
        return generator_func(num=rows)

    elif normalized_name == "jobdataset":
        return generator_func(num=rows)

    elif normalized_name == "healthcare":
        return generator_func(num=rows)

    return [generator_func() for _ in range(rows)]


if __name__ == "__main__":
    output = generate(dataset_name="Job dataset", rows=1000)
    print(len(output))
    print(output)
