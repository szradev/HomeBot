from homebot.modules.ci.projects.aosp.project import AOSPProject

class AospkProject(AOSPProject):
	name = "Aospk"
	category = "ROMs"
	lunch_prefix = "aospk"
	lunch_suffix = "userdebug"
	build_target = "bacon"
	artifacts = "AOSPk-*.zip"
	version = "11.0"
	android_version = "11"
