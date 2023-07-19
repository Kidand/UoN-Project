import nibabel as nib
import numpy as np

class ImageReaderWriter:
    def read_image(self, image_path):
        """
        Read an image file.

        Args:
            image_path (str): path to the image file.

        Returns:
            np.ndarray: the image array.
        """
        image = nib.load(image_path)
        return image.get_fdata()

    def write_image(self, image_path, image_data, affine=np.eye(4)):
        """
        Write an image file.

        Args:
            image_path (str): path to the image file.
            image_data (np.ndarray): the image data to write.
            affine (np.ndarray, optional): the affine transformation to associate with the image.
                Defaults to the identity transformation.
        """
        image = nib.Nifti1Image(image_data, affine)
        nib.save(image, image_path)

    def read_seg(self, seg_path):
        """
        Read a segmentation file. In this case, this is the same as reading an image file.

        Args:
            seg_path (str): path to the segmentation file.

        Returns:
            np.ndarray: the segmentation array.
        """
        return self.read_image(seg_path)

    def write_seg(self, seg_path, seg_data, affine=np.eye(4)):
        """
        Write a segmentation file. In this case, this is the same as writing an image file.

        Args:
            seg_path (str): path to the segmentation file.
            seg_data (np.ndarray): the segmentation data to write.
            affine (np.ndarray, optional): the affine transformation to associate with the image.
                Defaults to the identity transformation.
        """
        self.write_image(seg_path, seg_data, affine)
