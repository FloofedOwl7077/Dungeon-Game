from typing import Optional, Protocol

import tcod.event

from actions import Action, BumpAction, EscapeAction

class ActionHandler(Protocol):
    def handle_event(self, event: tcod.event.Event) -> Optional[Action]: ...


class EventHandler:
    def handle_event(self, event: tcod.event.Event) -> Optional[Action]:
        match event:
            case tcod.event.Quit():
                raise SystemExit()
            
            case tcod.event.KeyDown(sym=tcod.event.KeySym.UP):
                return BumpAction(dx=0, dy=-1)
            case tcod.event.KeyDown(sym=tcod.event.KeySym.DOWN):
                return BumpAction(dx=0, dy=1)
            case tcod.event.KeyDown(sym=tcod.event.KeySym.LEFT):
                return BumpAction(dx=-1, dy=0)
            case tcod.event.KeyDown(sym=tcod.event.KeySym.RIGHT):
                return BumpAction(dx=1, dy=0)
            
            case tcod.event.KeyDown(sym=tcod.event.KeySym.ESCAPE):
                return EscapeAction()
            
            case _:
                return None