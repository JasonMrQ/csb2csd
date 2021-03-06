# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuffers

import flatbuffers

class CSParseBinary(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsCSParseBinary(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CSParseBinary()
        x.Init(buf, n + offset)
        return x

    # CSParseBinary
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # CSParseBinary
    def Version(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # CSParseBinary
    def Textures(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # CSParseBinary
    def TexturesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CSParseBinary
    def TexturePngs(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # CSParseBinary
    def TexturePngsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CSParseBinary
    def NodeTree(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .NodeTree import NodeTree
            obj = NodeTree()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # CSParseBinary
    def Action(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .NodeAction import NodeAction
            obj = NodeAction()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # CSParseBinary
    def AnimationList(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .AnimationInfo import AnimationInfo
            obj = AnimationInfo()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # CSParseBinary
    def AnimationListLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def CSParseBinaryStart(builder): builder.StartObject(6)
def CSParseBinaryAddVersion(builder, version): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(version), 0)
def CSParseBinaryAddTextures(builder, textures): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(textures), 0)
def CSParseBinaryStartTexturesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def CSParseBinaryAddTexturePngs(builder, texturePngs): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(texturePngs), 0)
def CSParseBinaryStartTexturePngsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def CSParseBinaryAddNodeTree(builder, nodeTree): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(nodeTree), 0)
def CSParseBinaryAddAction(builder, action): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(action), 0)
def CSParseBinaryAddAnimationList(builder, animationList): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(animationList), 0)
def CSParseBinaryStartAnimationListVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def CSParseBinaryEnd(builder): return builder.EndObject()
