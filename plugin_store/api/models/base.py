from datetime import datetime
from typing import TYPE_CHECKING

from pydantic import BaseModel, Field
from pydantic.utils import ROOT_KEY

if TYPE_CHECKING:
    from typing import Any

    from pydantic.typing import DictStrAny


class PluginVersion(BaseModel):
    name: str
    hash: str


class BasePlugin(BaseModel):
    id: int
    name: str
    author: str
    description: str
    tags: list[str]
    versions: list[PluginVersion]
    visible: bool


class BasePluginRequest(BasePlugin):
    pass


class PluginTagResponse(BaseModel):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True

    __root__: str = Field(alias="tag")

    @classmethod
    def _enforce_dict_if_root(cls, obj: "Any") -> "Any":
        if cls.__custom_root_type__ and cls.__fields__[ROOT_KEY].alt_alias:
            return dict(cls._decompose_class(obj))

        return super()._enforce_dict_if_root(obj)

    def dict(self, **kwargs) -> "DictStrAny":
        if self.__custom_root_type__:
            kwargs["by_alias"] = False
            data = super().dict(**kwargs)
            return data[ROOT_KEY]
        return super().dict(**kwargs)


class PluginVersionResponse(PluginVersion):
    class Config:
        orm_mode = True

    created: datetime


class BasePluginResponse(BasePlugin):
    class Config:
        orm_mode = True

    tags: list[PluginTagResponse]  # type: ignore[assignment]
    versions: list[PluginVersionResponse]  # type: ignore[assignment]

    image_url: str
    created: datetime
    updated: datetime
