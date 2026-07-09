# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gordf
%define go_import_path  github.com/spdx/gordf
%define commit_id       7098f93598fb

Name:           go-github-spdx-gordf
Version:        0.0.0+git20201111.7098f93
Release:        %autorelease
Summary:        Go library packaged for syft dependency resolution
License:        MIT
URL:            https://github.com/spdx/gordf
#!RemoteAsset
Source0:        %{url}/archive/7098f93598fb.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-7098f93598fb

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/spdx/gordf) = %{version}

%description
Go library packaged for syft dependency resolution.

%files
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%{?autochangelog}
