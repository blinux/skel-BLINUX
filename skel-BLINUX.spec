#-
# Copyright 2013-2014 Emmanuel Vadot <elbarto@bocal.org>
# All rights reserved
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted providing that the following conditions 
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

Name:		skel-BLINUX
Version:        2.0
Release:        1
License:        BSD-2-Clause
Summary:	Skel BLINUX
Group:          System Environment/Base

BuildArch:      noarch
Source0:	Xdefaults
Source1:	bashrc
Source2:	emacs
Source3:	icewm_startup
Requires:	std-el

Packager:       Emmanuel Vadot <elbarto@bocal.org>
Url:            http://www.blinux.fr
Vendor:		Blinux

%description
Skel for BLINUX users

%prep

%build

%install
rm -fr %{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/skel-BLINUX/
mkdir -p %{buildroot}%{_sysconfdir}/skel-BLINUX/.icewm
install -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/skel-BLINUX/.Xdefaults
install -D -m 755 %{SOURCE1} %{buildroot}%{_sysconfdir}/skel-BLINUX/.bashrc
install -D -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/skel-BLINUX/.emacs
install -D -m 755 %{SOURCE3} %{buildroot}%{_sysconfdir}/skel-BLINUX/.icewm/startup

%files
%defattr(-,root,root)
%{_sysconfdir}/skel-BLINUX/
%{_sysconfdir}/skel-BLINUX/.icewm
%{_sysconfdir}/skel-BLINUX/.Xdefaults
%{_sysconfdir}/skel-BLINUX/.bashrc
%{_sysconfdir}/skel-BLINUX/.emacs
%{_sysconfdir}/skel-BLINUX/.icewm/startup

%changelog
* Mon Aug 04 2014 Emmanuel Vadot <elbarto@bocal.org> - 2.0-0
- Remove .xsession
- Bump to 2.0

* Thu Apr 10 2014 Emmanuel Vadot <elbarto@bocal.org> - 1.0.1-0
- Package creation

* Sat Mar 01 2014 Emmanuel Vadot <elbarto@bocal.org> - 1.0-0
- Package creation
