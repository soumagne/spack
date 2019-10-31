# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class ProtobufC(AutotoolsPackage):
    """
    Protocol Buffers implementation in C
    """

    homepage = "https://github.com/protobuf-c/protobuf-c"
    url      = "https://github.com/protobuf-c/protobuf-c/releases/download/v1.3.2/protobuf-c-1.3.2.tar.gz"
    git      = "https://github.com/protobuf-c/protobuf-c.git"

    version('master', branch='master')

    # Current
    version('1.3.3', sha256='22956606ef50c60de1fabc13a78fbc50830a0447d780467d3c519f84ad527e78')
    version('1.3.2', sha256='53f251f14c597bdb087aecf0b63630f434d73f5a10fc1ac545073597535b9e74')
    version('1.3.1', sha256='51472d3a191d6d7b425e32b612e477c06f73fe23e07f6a6a839b11808e9d2267')

    depends_on('autoconf', type='build', when='@master')
    depends_on('automake', type='build', when='@master')
    depends_on('libtool',  type='build', when='@master')
    depends_on('m4', type='build', when='@master')
    depends_on('protobuf')
    depends_on('pkgconfig', type='build')

    def configure_args(self):
        spec = self.spec
        config_args = [
            '--enable-shared',
        ]

        return config_args
