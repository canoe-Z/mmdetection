from mmdet.models.roi_heads.roi_extractors.single_level_roi_extractor import SingleRoIExtractor

from mmdet.registry import MODELS


@MODELS.register_module()
class SingleRoIExtractorWithScore(SingleRoIExtractor):
    """Extract RoI features from a single level feature map.

    If there are multiple input feature levels, each RoI is mapped to a level
    according to its scale. The mapping rule is proposed in
    `FPN <https://arxiv.org/abs/1612.03144>`_.

    Args:
        roi_layer (:obj:`ConfigDict` or dict): Specify RoI layer type and
            arguments.
        out_channels (int): Output channels of RoI layers.
        featmap_strides (List[int]): Strides of input feature maps.
        finest_scale (int): Scale threshold of mapping to level 0.
            Defaults to 56.
        init_cfg (:obj:`ConfigDict` or dict or list[:obj:`ConfigDict` or \
            dict], optional): Initialization config dict. Defaults to None.
    """

    def forward(self, feats, rois, roi_scale_factor=None):
        """Forward function.

        Args:
            feats (torch.Tensor): Input features.
            rois (torch.Tensor): Input RoIs, shape (k, 5).
            scale_factor (float): Scale factor that RoI will be multiplied by.

        Returns:
            torch.Tensor: Scaled RoI features.
        """
        rois = rois[:, :-1]
        return super().forward(feats, rois, roi_scale_factor)
