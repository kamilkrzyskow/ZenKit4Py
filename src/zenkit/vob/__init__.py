from zenkit.vob.cutscene_camera import CameraTrajectoryFrame
from zenkit.vob.cutscene_camera import CutsceneCamera
from zenkit.vob.light import Light
from zenkit.vob.misc import Animate
from zenkit.vob.misc import CodeMaster
from zenkit.vob.misc import Earthquake
from zenkit.vob.misc import Item
from zenkit.vob.misc import MessageFilter
from zenkit.vob.misc import MoverController
from zenkit.vob.misc import ParticleEffectController
from zenkit.vob.misc import TouchDamage
from zenkit.vob.virtual_object import VirtualObject
from zenkit.vob.virtual_object import VobType

_VOBS: dict[VobType, type[VirtualObject]] = {
    VobType.zCCSCamera: CutsceneCamera,
    VobType.zCCamTrj_KeyFrame: CameraTrajectoryFrame,
    VobType.zCVobLight: Light,
    VobType.zCVobAnimate: Animate,
    VobType.oCItem: Item,
    VobType.zCPFXController: ParticleEffectController,
    VobType.zCMessageFilter: MessageFilter,
    VobType.zCMoverController: MoverController,
    VobType.oCTouchDamage: TouchDamage,
    VobType.zCCodeMaster: CodeMaster,
    VobType.zCEarthquake: Earthquake,
}
