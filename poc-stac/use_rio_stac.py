import os

from rasterio import open as rio_open
from rio_stac import create_stac_item


def generate_stac_metadata(source, target):
    """
    Generates STAC metadata for a source TIFF file and saves it to target.

    Args:
        source: Path to the TIFF file.
        target: Directory where the STAC metadata will be saved.
    """
    # Ensure the output directory exists
    os.makedirs(target, exist_ok=True)

    # Open the GeoTIFF file with rasterio
    with rio_open(source) as src:
        # Create the STAC item
        stac_item = create_stac_item(
            src,
            geom_precision=8,
            asset_name="visual",
            id=os.path.basename(source).replace(".tiff", ""),
        )

    filename = os.path.join(target, f"{stac_item.id}.json")
    stac_item.set_self_href(filename)

    # Save the STAC item
    stac_item.save_object(filename)

    print(f"STAC metadata saved at: {filename}")


def main():
    source = "BH40_10000_0502.tiff"
    target = "output"

    print("Generating...")
    generate_stac_metadata(source, target)
    print("Done.")


if __name__ == "__main__":
    main()
