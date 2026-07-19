# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-securesystemslib
%define go_import_path  github.com/secure-systems-lab/go-securesystemslib

Name:           go-github-secure-systems-lab-go-securesystemslib
Version:        0.11.0
Release:        %autorelease
Summary:        A library that provides cryptographic and general-purpose functions for Go
License:        MIT
URL:            https://github.com/secure-systems-lab/go-securesystemslib
#!RemoteAsset:  sha256:2bf9c97afec8e45f5f4b68121ac747e14e76c887024000a4a8bebf463fe2d50e
Source0:        https://github.com/secure-systems-lab/go-securesystemslib/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/codahale/rfc6979)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/crypto)

Provides:       go(github.com/secure-systems-lab/go-securesystemslib) = %{version}

Requires:       go(github.com/codahale/rfc6979)
Requires:       go(github.com/stretchr/testify)
Requires:       go(golang.org/x/crypto)

%description
A library that provides cryptographic and general-purpose functions for
Go Secure Systems Lab projects at NYU.

go-securesystemslib is used in quite a few places. Below are the top 50
dependents sorted by GitHub stars as of Jan 8th, 2026 as is reported by
GitHub's dependents.

 Repository                                     | Stars
------------------------------------------------+---------------------
 moby/moby                                      | 71324
 docker/compose                                 | 36769
 1Panel-dev/1Panel                              | 32786
 gravitational/teleport                         | 19636
 kubernetes/kops                                | 16529
 GoogleContainerTools/skaffold                  | 15687
 dagger/dagger                                  | 15242
 OpenNHP/opennhp                                | 13738
 Canner/WrenAI                                  | 13422
 kubescape/kubescape                            | 11130
 containers/skopeo                              | 10268
 moby/buildkit                                  | 9646
 getlago/lago                                   | 9021
 tektoncd/pipeline                              | 8848
 operator-framework/operator-sdk                | 7585
 BoundaryML/baml                                | 7293
 alibaba/higress                                | 7251
 sigstore/cosign                                | 5556
 cri-o/cri-o                                    | 5555
 kgateway-dev/kgateway                          | 5200
 confluentinc/confluent-kafka-go                | 5081
 jitsucom/jitsu                                 | 4621
 open-telemetry/opentelemetry-collector-contrib | 4289
 docker/buildx                                  | 4221
 cerbos/cerbos                                  | 4183
 odigos-io/odigos                               | 3606
 getarcaneapp/arcane                            | 3530
 okteto/okteto                                  | 3479
 DataDog/datadog-agent                          | 3452
 yandex/perforator                              | 3380
 ddworken/hishtory                              | 2994
 inspektor-gadget/inspektor-gadget              | 2675
 openflagr/flagr                                | 2565
 sablierapp/sablier                             | 2464
 srl-labs/containerlab                          | 2338
 tensorchord/envd                               | 2173
 artifacthub/hub                                | 1977
 shellhub-io/shellhub                           | 1870
 zarf-dev/zarf                                  | 1784
 julien040/anyquery                             | 1582
 inverse-inc/packetfence                        | 1572
 ktock/buildg                                   | 1482
 lunasec-io/lunasec                             | 1462
 openclarity/openclarity                        | 1444
 controlplaneio/kubesec                         | 1424
 getporter/porter                               | 1374
 sigstore/rekor                                 | 1059
 sigstore/gitsign                               | 1051
 containers/podman-tui                          | 1010
 containers/image                               | 949

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
