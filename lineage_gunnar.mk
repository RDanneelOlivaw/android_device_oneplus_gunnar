#
# Copyright (C) 2021-2024 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit from gunnar device
$(call inherit-product, device/oneplus/gunnar/device.mk)

# Inherit some common Lineage stuff.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

PRODUCT_NAME := lineage_gunnar
PRODUCT_DEVICE := gunnar
PRODUCT_MANUFACTURER := OnePlus
PRODUCT_BRAND := OnePlus
PRODUCT_MODEL := CPH2459

PRODUCT_GMS_CLIENTID_BASE := android-oneplus

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc="CPH2459-user 12 RKQ1.211119.001 1863297-1adfc-a2c6b release-keys" \
    BuildFingerprint=OnePlus/CPH2459/OP5159L1:12/RKQ1.211119.001/1863297-1adfc-a2c6b:user/release-keys \
    DeviceName=OP5159L1 \
    DeviceProduct=CPH2459 \
    SystemDevice=OP5159L1 \
    SystemName=CPH2459
