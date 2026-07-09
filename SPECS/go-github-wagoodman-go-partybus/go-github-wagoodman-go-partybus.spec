# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-partybus
%define go_import_path  github.com/wagoodman/go-partybus
%define commit_id       8ccac152c651

Name:           go-github-wagoodman-go-partybus
Version:        0.0.0+git20230516.8ccac15
Release:        %autorelease
Summary:        Go library packaged for syft dependency resolution
License:        MIT
URL:            https://github.com/wagoodman/go-partybus
#!RemoteAsset
Source0:        %{url}/archive/8ccac152c651.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-8ccac152c651

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/wagoodman/go-partybus) = %{version}

%description
Go library packaged for syft dependency resolution.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%{?autochangelog}
