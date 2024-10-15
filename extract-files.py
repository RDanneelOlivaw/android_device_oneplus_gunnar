#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'vendor/oneplus/sm6375-common',
]

blob_fixups: blob_fixups_user_type = {
    'vendor/lib64/sensors.ssc.so': blob_fixup()
        .regex_replace('qti.sensor.wise_light', 'android.sensor.light')
        .sig_replace('EA D3 84 52 01 41 00 91 29 00 15 CB 29 41 00 D1 29 15 C9 93 4A 3F A0 72', 'AA 00 80 52 01 41 00 91 29 00 15 CB 29 41 00 D1 29 15 C9 93 0A 00 A0 72'),
}  # fmt: skip

module = ExtractUtilsModule(
    'gunnar',
    'oneplus',
    namespace_imports=namespace_imports,
    blob_fixups=blob_fixups,
    add_firmware_proprietary_file=True,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'sm6375-common', module.vendor
    )
    utils.run()
