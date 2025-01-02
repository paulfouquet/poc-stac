import os

from stactools.core.create import item


def generate_stac_metadata(source, target):
    """
    Generates STAC metadata for a source TIFF file and saves it to target.

    Parameters:
        source: Path to the TIFF file.
        target: Directory where the STAC metadata will be saved.
    """
    # Ensure output directory exists
    os.makedirs(target, exist_ok=True)

    # Create a STAC item from the GeoTIFF file
    stac_item = item(source, asset_key="visual", roles=["visual"])
    filename = os.path.join(target, f"{stac_item.id}.json")
    stac_item.set_self_href(filename)

    # Save the STAC item as a JSON file
    item_path = os.path.join(target, filename)
    stac_item.save_object(item_path)

    print(f"STAC metadata saved at: {item_path}")


def main():
    source = "BH40_10000_0502.tiff"
    target = "output"

    print("Generating...")
    generate_stac_metadata(source, target)
    print("Done")


if __name__ == "__main__":
    main()
