# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sqlite
%define go_import_path  modernc.org/sqlite

Name:           go-modernc-sqlite
Version:        1.51.0
Release:        %autorelease
Summary:        Go SQLite database driver
License:        BSD-3-Clause
URL:            https://gitlab.com/cznic/sqlite
#!RemoteAsset
Source0:        %{url}/-/archive/v%{version}/sqlite-v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-v%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(modernc.org/sqlite) = %{version}

%description
This package provides a Go SQLite database driver.

%files
%license LICENSE
%doc README.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%{?autochangelog}
