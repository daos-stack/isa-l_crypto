NAME    := isa-l_crypto
DEB_NAME := libisal_crypto
SRC_EXT := gz
SOURCE   = https://github.com/intel/$(NAME)/archive/v$(VERSION).tar.$(SRC_EXT)

include Makefile_packaging.mk

