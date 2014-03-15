# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'variables': {
    'chromium_code': 1,
  },
  'includes': [
    'chromeos_memory.gypi',
    'chromeos_tools.gypi',
  ],
  'targets': [
    {
      'target_name': 'chromeos',
      'type': '<(component)',
      'dependencies': [
        '../base/base.gyp:base',
        '../base/base.gyp:base_prefs',
        '../components/components.gyp:onc_component',
        '../crypto/crypto.gyp:crypto',
        '../base/third_party/dynamic_annotations/dynamic_annotations.gyp:dynamic_annotations',
        '../build/linux/system.gyp:dbus',
        '../build/linux/system.gyp:ssl',
        '../dbus/dbus.gyp:dbus',
        '../net/net.gyp:net',
        '../third_party/icu/icu.gyp:icui18n',
        '../third_party/libxml/libxml.gyp:libxml',
        '../url/url.gyp:url_lib',
        'cryptohome_proto',
        'ime/input_method.gyp:gencode',
        'power_manager_proto',
      ],
      'defines': [
        'CHROMEOS_IMPLEMENTATION',
      ],
      'sources': [
        'app_mode/kiosk_oem_manifest_parser.cc',
        'app_mode/kiosk_oem_manifest_parser.h',
        'audio/audio_device.cc',
        'audio/audio_device.h',
        'audio/audio_devices_pref_handler.h',
        'audio/audio_pref_observer.h',
        'audio/cras_audio_handler.cc',
        'audio/cras_audio_handler.h',
        'audio/audio_devices_pref_handler_stub.cc',
        'audio/audio_devices_pref_handler_stub.h',
        'audio/chromeos_sounds.h',
        'attestation/attestation_constants.cc',
        'attestation/attestation_constants.h',
        'attestation/attestation_flow.cc',
        'attestation/attestation_flow.h',
        'cert_loader.cc',
        'cert_loader.h',
        'chromeos_constants.cc',
        'chromeos_constants.h',
        'chromeos_export.h',
        'chromeos_paths.cc',
        'chromeos_paths.h',
        'chromeos_switches.cc',
        'chromeos_switches.h',
        'cryptohome/cryptohome_parameters.cc',
        'cryptohome/cryptohome_parameters.h',
        'cryptohome/homedir_methods.cc',
        'cryptohome/homedir_methods.h',
        'cryptohome/async_method_caller.cc',
        'cryptohome/async_method_caller.h',
        'cryptohome/cryptohome_util.cc',
        'cryptohome/cryptohome_util.h',
        'cryptohome/system_salt_getter.cc',
        'cryptohome/system_salt_getter.h',
        'dbus/audio_node.cc',
        'dbus/audio_node.h',
        'dbus/blocking_method_caller.cc',
        'dbus/blocking_method_caller.h',
        'dbus/bluetooth_adapter_client.cc',
        'dbus/bluetooth_adapter_client.h',
        'dbus/bluetooth_agent_manager_client.cc',
        'dbus/bluetooth_agent_manager_client.h',
        'dbus/bluetooth_agent_service_provider.cc',
        'dbus/bluetooth_agent_service_provider.h',
        'dbus/bluetooth_device_client.cc',
        'dbus/bluetooth_device_client.h',
        'dbus/bluetooth_input_client.cc',
        'dbus/bluetooth_input_client.h',
        'dbus/bluetooth_profile_manager_client.cc',
        'dbus/bluetooth_profile_manager_client.h',
        'dbus/bluetooth_profile_service_provider.cc',
        'dbus/bluetooth_profile_service_provider.h',
        'dbus/cras_audio_client.cc',
        'dbus/cras_audio_client.h',
        'dbus/cras_audio_client_stub_impl.cc',
        'dbus/cras_audio_client_stub_impl.h',
        'dbus/cros_disks_client.cc',
        'dbus/cros_disks_client.h',
        'dbus/cryptohome_client.cc',
        'dbus/cryptohome_client.h',
        'dbus/dbus_client_implementation_type.h',
        'dbus/dbus_method_call_status.cc',
        'dbus/dbus_method_call_status.h',
        'dbus/dbus_thread_manager.cc',
        'dbus/dbus_thread_manager.h',
        'dbus/debug_daemon_client.cc',
        'dbus/debug_daemon_client.h',
        'dbus/fake_bluetooth_adapter_client.cc',
        'dbus/fake_bluetooth_adapter_client.h',
        'dbus/fake_bluetooth_agent_manager_client.cc',
        'dbus/fake_bluetooth_agent_manager_client.h',
        'dbus/fake_bluetooth_agent_service_provider.cc',
        'dbus/fake_bluetooth_agent_service_provider.h',
        'dbus/fake_bluetooth_device_client.cc',
        'dbus/fake_bluetooth_device_client.h',
        'dbus/fake_bluetooth_input_client.cc',
        'dbus/fake_bluetooth_input_client.h',
        'dbus/fake_bluetooth_profile_manager_client.cc',
        'dbus/fake_bluetooth_profile_manager_client.h',
        'dbus/fake_bluetooth_profile_service_provider.cc',
        'dbus/fake_bluetooth_profile_service_provider.h',
        'dbus/fake_cryptohome_client.cc',
        'dbus/fake_cryptohome_client.h',
        'dbus/fake_dbus_thread_manager.cc',
        'dbus/fake_dbus_thread_manager.h',
        'dbus/fake_debug_daemon_client.cc',
        'dbus/fake_debug_daemon_client.h',
        'dbus/fake_gsm_sms_client.cc',
        'dbus/fake_gsm_sms_client.h',
        'dbus/fake_introspectable_client.cc',
        'dbus/fake_introspectable_client.h',
        'dbus/fake_modem_messaging_client.cc',
        'dbus/fake_modem_messaging_client.h',
        'dbus/fake_nfc_adapter_client.cc',
        'dbus/fake_nfc_adapter_client.h',
        'dbus/fake_nfc_device_client.cc',
        'dbus/fake_nfc_device_client.h',
        'dbus/fake_nfc_manager_client.cc',
        'dbus/fake_nfc_manager_client.h',
        'dbus/fake_nfc_record_client.cc',
        'dbus/fake_nfc_record_client.h',
        'dbus/fake_nfc_tag_client.cc',
        'dbus/fake_nfc_tag_client.h',
        'dbus/fake_image_burner_client.cc',
        'dbus/fake_image_burner_client.h',
        'dbus/fake_permission_broker_client.cc',
        'dbus/fake_permission_broker_client.h',
        'dbus/fake_shill_device_client.cc',
        'dbus/fake_shill_device_client.h',
        'dbus/fake_shill_ipconfig_client.cc',
        'dbus/fake_shill_ipconfig_client.h',
        'dbus/fake_shill_manager_client.cc',
        'dbus/fake_shill_manager_client.h',
        'dbus/fake_shill_profile_client.cc',
        'dbus/fake_shill_profile_client.h',
        'dbus/fake_shill_service_client.cc',
        'dbus/fake_shill_service_client.h',
        'dbus/fake_sms_client.cc',
        'dbus/fake_sms_client.h',
        'dbus/fake_system_clock_client.cc',
        'dbus/fake_system_clock_client.h',
        'dbus/gsm_sms_client.cc',
        'dbus/gsm_sms_client.h',
        'dbus/nfc_adapter_client.cc',
        'dbus/nfc_adapter_client.h',
        'dbus/nfc_client_helpers.cc',
        'dbus/nfc_client_helpers.h',
        'dbus/nfc_device_client.cc',
        'dbus/nfc_device_client.h',
        'dbus/nfc_manager_client.cc',
        'dbus/nfc_manager_client.h',
        'dbus/nfc_property_set.cc',
        'dbus/nfc_property_set.h',
        'dbus/nfc_record_client.cc',
        'dbus/nfc_record_client.h',
        'dbus/nfc_tag_client.cc',
        'dbus/nfc_tag_client.h',
        'dbus/shill_client_helper.cc',
        'dbus/shill_client_helper.h',
        'dbus/shill_device_client.cc',
        'dbus/shill_device_client.h',
        'dbus/shill_ipconfig_client.cc',
        'dbus/shill_ipconfig_client.h',
        'dbus/shill_manager_client.cc',
        'dbus/shill_manager_client.h',
        'dbus/shill_profile_client.cc',
        'dbus/shill_profile_client.h',
        'dbus/shill_service_client.cc',
        'dbus/shill_service_client.h',
        'dbus/image_burner_client.cc',
        'dbus/image_burner_client.h',
        'dbus/introspectable_client.cc',
        'dbus/introspectable_client.h',
        'dbus/modem_messaging_client.cc',
        'dbus/modem_messaging_client.h',
        'dbus/permission_broker_client.cc',
        'dbus/permission_broker_client.h',
        'dbus/power_manager_client.cc',
        'dbus/power_manager_client.h',
        'dbus/power_policy_controller.cc',
        'dbus/power_policy_controller.h',
        'dbus/session_manager_client.cc',
        'dbus/session_manager_client.h',
        'dbus/sms_client.cc',
        'dbus/sms_client.h',
        'dbus/system_clock_client.cc',
        'dbus/system_clock_client.h',
        'dbus/update_engine_client.cc',
        'dbus/update_engine_client.h',
        'dbus/volume_state.cc',
        'dbus/volume_state.h',
        'disks/disk_mount_manager.cc',
        'disks/disk_mount_manager.h',
        'ime/component_extension_ime_manager.cc',
        'ime/component_extension_ime_manager.h',
        'ime/extension_ime_util.cc',
        'ime/extension_ime_util.h',
        'ime/fake_xkeyboard.cc',
        'ime/fake_xkeyboard.h',
        'ime/composition_text.cc',
        'ime/composition_text.h',
        'ime/input_method_delegate.h',
        'ime/input_method_descriptor.cc',
        'ime/input_method_descriptor.h',
        'ime/input_method_manager.cc',
        'ime/input_method_manager.h',
        'ime/input_method_whitelist.cc',
        'ime/input_method_whitelist.h',
        'ime/xkeyboard.cc',
        'ime/xkeyboard.h',
        'login/login_state.cc',
        'login/login_state.h',
        'network/certificate_pattern.cc',
        'network/certificate_pattern.h',
        'network/client_cert_resolver.cc',
        'network/client_cert_resolver.h',
        'network/client_cert_util.cc',
        'network/client_cert_util.h',
        'network/device_state.cc',
        'network/device_state.h',
        'network/favorite_state.cc',
        'network/favorite_state.h',
        'network/geolocation_handler.cc',
        'network/geolocation_handler.h',
        'network/managed_network_configuration_handler.cc',
        'network/managed_network_configuration_handler.h',
        'network/managed_network_configuration_handler_impl.cc',
        'network/managed_network_configuration_handler_impl.h',
        'network/managed_state.cc',
        'network/managed_state.h',
	'network/network_activation_handler.cc',
	'network/network_activation_handler.h',
        'network/network_cert_migrator.cc',
        'network/network_cert_migrator.h',
        'network/network_change_notifier_chromeos.cc',
        'network/network_change_notifier_chromeos.h',
        'network/network_change_notifier_factory_chromeos.cc',
        'network/network_change_notifier_factory_chromeos.h',
        'network/network_configuration_handler.cc',
        'network/network_configuration_handler.h',
        'network/network_connection_handler.cc',
        'network/network_connection_handler.h',
        'network/network_device_handler.cc',
        'network/network_device_handler.h',
        'network/network_device_handler_impl.cc',
        'network/network_device_handler_impl.h',
        'network/network_event_log.cc',
        'network/network_event_log.h',
        'network/network_handler.cc',
        'network/network_handler.h',
        'network/network_handler_callbacks.cc',
        'network/network_handler_callbacks.h',
        'network/network_ip_config.cc',
        'network/network_ip_config.h',
        'network/network_profile.cc',
        'network/network_profile.h',
        'network/network_profile_handler.cc',
        'network/network_profile_handler.h',
        'network/network_profile_observer.h',
        'network/network_sms_handler.cc',
        'network/network_sms_handler.h',
        'network/network_state.cc',
        'network/network_state.h',
        'network/network_state_handler.cc',
        'network/network_state_handler.h',
        'network/network_state_handler_observer.cc',
        'network/network_state_handler_observer.h',
        'network/network_ui_data.cc',
        'network/network_ui_data.h',
        'network/network_util.cc',
        'network/network_util.h',
        'network/onc/onc_certificate_importer.h',
        'network/onc/onc_certificate_importer_impl.cc',
        'network/onc/onc_certificate_importer_impl.h',
        'network/onc/onc_mapper.cc',
        'network/onc/onc_mapper.h',
        'network/onc/onc_merger.cc',
        'network/onc/onc_merger.h',
        'network/onc/onc_normalizer.cc',
        'network/onc/onc_normalizer.h',
        'network/onc/onc_signature.cc',
        'network/onc/onc_signature.h',
        'network/onc/onc_translation_tables.cc',
        'network/onc/onc_translation_tables.h',
        'network/onc/onc_translator.h',
        'network/onc/onc_translator_onc_to_shill.cc',
        'network/onc/onc_translator_shill_to_onc.cc',
        'network/onc/onc_utils.cc',
        'network/onc/onc_utils.h',
        'network/onc/onc_validator.cc',
        'network/onc/onc_validator.h',
        'network/policy_util.cc',
        'network/policy_util.h',
        'network/policy_applicator.cc',
        'network/policy_applicator.h',
        'network/shill_property_handler.cc',
        'network/shill_property_handler.h',
        'network/shill_property_util.cc',
        'network/shill_property_util.h',
        'network/dhcp_proxy_script_fetcher_chromeos.cc',
        'network/dhcp_proxy_script_fetcher_chromeos.h',
        'process_proxy/process_output_watcher.cc',
        'process_proxy/process_output_watcher.h',
        'process_proxy/process_proxy.cc',
        'process_proxy/process_proxy.h',
        'process_proxy/process_proxy_registry.cc',
        'process_proxy/process_proxy_registry.h',
        'settings/cros_settings_names.cc',
        'settings/cros_settings_names.h',
        'settings/cros_settings_provider.cc',
        'settings/cros_settings_provider.h',
        'settings/timezone_settings.cc',
        'settings/timezone_settings.h',
        'system/name_value_pairs_parser.cc',
        'system/name_value_pairs_parser.h',
        'system/statistics_provider.cc',
        'system/statistics_provider.h',
        'tpm_token_loader.cc',
        'tpm_token_loader.h'
      ],
      'conditions': [
        ['use_x11 == 1', {
          'dependencies': [
            '../build/linux/system.gyp:x11',
          ],
        }, {
          # use_x11 == 0
          'sources!': [
            'ime/xkeyboard.cc',
            'ime/xkeyboard.h',
          ],
        }],
      ],
    },
    {
      # This target contains mocks that can be used to write unit tests.
      'target_name': 'chromeos_test_support',
      'type': 'static_library',
      'dependencies': [
        '../build/linux/system.gyp:dbus',
        '../testing/gmock.gyp:gmock',
        'chromeos',
        'chromeos_test_support_without_gmock',
        'cryptohome_proto',
        'power_manager_proto',
      ],
      'sources': [
        'attestation/mock_attestation_flow.cc',
        'attestation/mock_attestation_flow.h',
        'chromeos_test_utils.cc',
        'chromeos_test_utils.h',
        'cryptohome/mock_async_method_caller.cc',
        'cryptohome/mock_async_method_caller.h',
        'cryptohome/mock_homedir_methods.cc',
        'cryptohome/mock_homedir_methods.h',
        'dbus/mock_cryptohome_client.cc',
        'dbus/mock_cryptohome_client.h',
        'dbus/mock_session_manager_client.cc',
        'dbus/mock_session_manager_client.h',
        'dbus/mock_shill_manager_client.cc',
        'dbus/mock_shill_manager_client.h',
        'dbus/mock_shill_profile_client.cc',
        'dbus/mock_shill_profile_client.h',
        'dbus/mock_shill_service_client.cc',
        'dbus/mock_shill_service_client.h',
        'disks/mock_disk_mount_manager.cc',
        'disks/mock_disk_mount_manager.h',
        'ime/mock_component_extension_ime_manager_delegate.cc',
        'ime/mock_component_extension_ime_manager_delegate.h',
        'network/fake_network_device_handler.cc',
        'network/fake_network_device_handler.h',
        'network/mock_managed_network_configuration_handler.cc',
        'network/mock_managed_network_configuration_handler.h',
        'network/onc/mock_certificate_importer.cc',
        'network/onc/mock_certificate_importer.h',
        'network/onc/onc_test_utils.cc',
        'network/onc/onc_test_utils.h',
        'system/mock_statistics_provider.cc',
        'system/mock_statistics_provider.h',
      ],
      'include_dirs': [
        '..',
      ],
    },
    {
      'target_name': 'chromeos_test_support_without_gmock',
      'type': 'static_library',
      'dependencies': [
        '../build/linux/system.gyp:dbus',
        '../crypto/crypto.gyp:crypto',
        '../dbus/dbus.gyp:dbus',
        'chromeos',
        'cryptohome_proto',
        'power_manager_proto',
      ],
      'sources': [
        'dbus/fake_cros_disks_client.cc',
        'dbus/fake_cros_disks_client.h',
        'dbus/fake_power_manager_client.cc',
        'dbus/fake_power_manager_client.h',
        'dbus/fake_session_manager_client.cc',
        'dbus/fake_session_manager_client.h',
        'dbus/fake_shill_manager_client.cc',
        'dbus/fake_shill_manager_client.h',
        'dbus/fake_update_engine_client.cc',
        'dbus/fake_update_engine_client.h',
        'ime/fake_input_method_delegate.cc',
        'ime/fake_input_method_delegate.h',
      ],
      'include_dirs': [
        '..',
      ],
    },
    {
      'target_name': 'chromeos_unittests',
      'type': 'executable',
      'dependencies': [
        '../base/base.gyp:run_all_unittests',
        '../base/base.gyp:test_support_base',
        '../build/linux/system.gyp:dbus',
        '../build/linux/system.gyp:ssl',
        '../components/components.gyp:onc_component',
        '../crypto/crypto.gyp:crypto',
        '../dbus/dbus.gyp:dbus_test_support',
        '../net/net.gyp:net',
        '../net/net.gyp:net_test_support',
        '../testing/gmock.gyp:gmock',
        '../testing/gtest.gyp:gtest',
        '../url/url.gyp:url_lib',
        'chromeos_test_support',
        'cryptohome_proto',
        'power_manager_proto',
      ],
      'sources': [
        'app_mode/kiosk_oem_manifest_parser_unittest.cc',
        'attestation/attestation_flow_unittest.cc',
        'audio/cras_audio_handler_unittest.cc',
        'cert_loader_unittest.cc',
        'cryptohome/system_salt_getter_unittest.cc',
        'dbus/blocking_method_caller_unittest.cc',
        'dbus/cros_disks_client_unittest.cc',
        'dbus/gsm_sms_client_unittest.cc',
        'dbus/introspectable_client_unittest.cc',
        'dbus/modem_messaging_client_unittest.cc',
        'dbus/nfc_client_unittest.cc',
        'dbus/power_policy_controller_unittest.cc',
        'dbus/shill_client_unittest_base.cc',
        'dbus/shill_client_unittest_base.h',
        'dbus/shill_device_client_unittest.cc',
        'dbus/shill_ipconfig_client_unittest.cc',
        'dbus/shill_manager_client_unittest.cc',
        'dbus/shill_profile_client_unittest.cc',
        'dbus/shill_service_client_unittest.cc',
        'disks/disk_mount_manager_unittest.cc',
        'ime/component_extension_ime_manager_unittest.cc',
        'ime/extension_ime_util_unittest.cc',
        'ime/composition_text_unittest.cc',
        'ime/input_method_manager.h',
        'ime/input_method_whitelist_unittest.cc',
        'ime/xkeyboard_unittest.cc',
        'login/login_state_unittest.cc',
        'network/client_cert_resolver_unittest.cc',
        'network/geolocation_handler_unittest.cc',
        'network/managed_network_configuration_handler_unittest.cc',
        'network/network_cert_migrator_unittest.cc',
        'network/network_change_notifier_chromeos_unittest.cc',
        'network/network_configuration_handler_unittest.cc',
        'network/network_connection_handler_unittest.cc',
        'network/network_device_handler_unittest.cc',
        'network/network_event_log_unittest.cc',
        'network/network_profile_handler_stub.h',
        'network/network_sms_handler_unittest.cc',
        'network/network_state_handler_unittest.cc',
        'network/network_state_unittest.cc',
        'network/network_ui_data_unittest.cc',
        'network/network_util_unittest.cc',
        'network/onc/onc_certificate_importer_impl_unittest.cc',
        'network/onc/onc_merger_unittest.cc',
        'network/onc/onc_normalizer_unittest.cc',
        'network/onc/onc_translator_unittest.cc',
        'network/onc/onc_utils_unittest.cc',
        'network/onc/onc_validator_unittest.cc',
        'network/shill_property_handler_unittest.cc',
        'network/shill_property_util_unittest.cc',
        'process_proxy/process_output_watcher_unittest.cc',
        'process_proxy/process_proxy_unittest.cc',
        'system/name_value_pairs_parser_unittest.cc',
      ],
      'include_dirs': [
        '..',
      ],
      'conditions': [
        # TODO(dmikurube): Kill linux_use_tcmalloc. http://crbug.com/345554
        [ '(use_allocator!="none" and use_allocator!="see_use_tcmalloc") or (use_allocator=="see_use_tcmalloc" and linux_use_tcmalloc==1)', {
           'dependencies': [
              '../base/allocator/allocator.gyp:allocator',
            ],
          },
        ],
      ],
    },
    {
      # Protobuf compiler/generator for power-manager related protocol buffers.
      'target_name': 'power_manager_proto',
      'type': 'static_library',
      'sources': [
        '../third_party/cros_system_api/dbus/power_manager/input_event.proto',
        '../third_party/cros_system_api/dbus/power_manager/peripheral_battery_status.proto',
        '../third_party/cros_system_api/dbus/power_manager/policy.proto',
        '../third_party/cros_system_api/dbus/power_manager/power_supply_properties.proto',
        '../third_party/cros_system_api/dbus/power_manager/suspend.proto',
      ],
      'variables': {
        'proto_in_dir': '../third_party/cros_system_api/dbus/power_manager',
        'proto_out_dir': 'chromeos/dbus/power_manager',
      },
      'includes': ['../build/protoc.gypi'],
    },
    {
      # Protobuf compiler/generator for cryptohome related protocol buffers.
      'target_name': 'cryptohome_proto',
      'type': 'static_library',
      'sources': [
        '../third_party/cros_system_api/dbus/cryptohome/key.proto',
        '../third_party/cros_system_api/dbus/cryptohome/rpc.proto',
      ],
      'variables': {
        'proto_in_dir': '../third_party/cros_system_api/dbus/cryptohome',
        'proto_out_dir': 'chromeos/dbus/cryptohome',
      },
      'includes': ['../build/protoc.gypi'],
    },
  ],
}
