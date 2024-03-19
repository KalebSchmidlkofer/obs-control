import sys
import time
import logging

sys.path.append('../')
# from obswebsocket import obsws, requests  # noqa: E402
import obsws_python as obsws
# logging.basicConfig(level=logging.DEBUG)

class obs:
  host = "localhost"
  port = 4455
  password = "secret"

  # ws = obsws(host, port, password)
  cl = obsws.ReqClient(host=host, port=port, password=password, timeout=3)
  # ws.connect()
  class requests:

    def change_scene(scene_name):
      obs.cl.set_current_program_scene(scene_name)

      return {'status': 'success'}

    def list_scenes():
      resp = obs.cl.get_scene_list()
      scenes = [di.get("sceneName") for di in reversed(resp.scenes)]

      return scenes

    def active_scene():
      resp = obs.cl.get_current_program_scene()

      return resp.current_program_scene_name

  class Observer:
      def __init__(self):
          self._client = obsws.EventClient()
          self._client.callback.register(
              [
                  self.on_current_program_scene_changed,
                  self.on_scene_created,
                  self.on_input_mute_state_changed,
                  self.on_exit_started,
              ]
          )
          print(f"Registered events: {self._client.callback.get()}")
          self.running = True

      def on_current_program_scene_changed(self, data):
          """The current program scene has changed."""
          print(f"Switched to scene {data.scene_name}")

      def on_scene_created(self, data):
          """A new scene has been created."""
          print(f"scene {data.scene_name} has been created")

      def on_input_mute_state_changed(self, data):
          """An input's mute state has changed."""
          print(f"{data.input_name} mute toggled")

      def on_exit_started(self, _):
          """OBS has begun the shutdown process."""
          print(f"OBS closing!")
          self._client.unsubscribe()
          self.running = False
          