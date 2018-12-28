require 'xcodeproj'
project_path='some.xcodeproj'
project=Xcodeproj::Project.open(project_path)

target = project.targets.first

#Debug
debug = target.build_configurations.first
debug.build_settings['DEVELOPMENT_TEAM'] = 'teamIdNorName'
debug.build_settings['PROVISIONING_PROFILE_SPECIFIER'] = 'profileNameNorId'

#Release 
release = target.build_configurations.last
release.build_settings['DEVELOPMENT_TEAM'] = 'teamIdNorName'
release.build_settings['PROVISIONING_PROFILE_SPECIFIER'] = 'profileNameNorId'

project.save() 
