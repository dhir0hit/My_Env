import uuid


class Notes:
    def __init__(self,
                 _id,
                 _heading,
                 _body):
        self._id_ = uuid.uuid1() if _id is None else _id
        self._heading_ = _heading
        self._body_ = _body

    def set_heading(self, heading):
        self._heading_ = heading

    def Heading(self):
        return self._heading_

    def body(self, body):
        self._body_ = body
