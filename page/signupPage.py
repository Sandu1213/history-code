import os,sys
from importlib import reload
from common import bases
from elements.elements import Homepage
from common.common_func import common
src_path = os.path.abspath('..')
sys.path.append(src_path)
reload(sys)
cfg = common.read_yaml_config()

class signupPage(bases.bases):
	def signup_with_empty_username(self):
		pass

	def logout(self):
		self.click(Homepage.avator)		
		self.click(Homepage.exit)