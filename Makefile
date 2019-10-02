NAME    := isa-l_crypto
DEB_NAME := libisal-crypto
SRC_EXT := gz
SOURCE   = https://github.com/intel/$(NAME)/archive/v$(VERSION).tar.$(SRC_EXT)

include packaging/Makefile_packaging.mk
