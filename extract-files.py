#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_vendorcompat,
    lib_fixups_user_type,
    libs_proto_3_9_1,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'hardware/oplus',
    'vendor/oneplus/sm6375-common',
    'vendor/qcom/opensource/display',
]

lib_fixups: lib_fixups_user_type = {
    libs_proto_3_9_1: lib_fixup_vendorcompat,
}

blob_fixups: blob_fixups_user_type = {
    ('odm/lib/liblvimfs_wrapper.so', 'odm/lib64/libCOppLceTonemapAPI.so', 'odm/lib64/libaps_frame_registration.so', 'vendor/lib64/libalsc.so'): blob_fixup()
        .replace_needed('libstdc++.so', 'libstdc++_vendor.so'),
    'vendor/lib64/sensors.ssc.so': blob_fixup()
        .regex_replace('qti.sensor.wise_light', 'android.sensor.light')
        .sig_replace('EA D3 84 52 01 41 00 91 29 00 15 CB 29 41 00 D1 29 15 C9 93 4A 3F A0 72', 'AA 00 80 52 01 41 00 91 29 00 15 CB 29 41 00 D1 29 15 C9 93 0A 00 A0 72'),
}  # fmt: skip

module = ExtractUtilsModule(
    'gunnar',
    'oneplus',
    namespace_imports=namespace_imports,
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    check_elf=True,
    add_firmware_proprietary_file=True,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'sm6375-common', module.vendor
    )
    utils.run()
