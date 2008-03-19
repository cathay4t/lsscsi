#
# spec file for lsscsi
# 
# please send bugfixes or comments to dgilbert@interlog.com
#

Summary: List all SCSI devices (or hosts) and associated information
Name: lsscsi
Version: 0.08
Release: 1
Packager: dgilbert@interlog.com
License: GPL
Group: Utilities/System
Source: ftp://www.torque.net/scsi/lsscsi-0.08.tgz
Url: http://www.torque.net/scsi/lsscsi.html
Provides: lsscsi

%description
Uses information provided by sysfs in Linux kernel from around 2.5.50
to list all SCSI devices (or hosts).

Author:
--------
    Doug Gilbert <dgilbert@interlog.com>

%prep
%setup

%build
make

%install
make install INSTDIR=%{_bindir} MANDIR=%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(-,root,root) %doc README CHANGELOG INSTALL
%attr(755,root,root) %{_bindir}/lsscsi
%attr(-,root,root) %doc %{_mandir}/man8/lsscsi.8.gz
 

%changelog
* Sun Mar 2 2003 - dgilbert@interlog.com
- start to add host listing support (lk >= 2.5.63)
  * lsscsi-0.07
* Fri Feb 14 2003 - dgilbert@interlog.com
- queue_depth name change in sysfs (lk 2.5.60)
  * lsscsi-0.07
* Mon Jan 20 2003 - dgilbert@interlog.com
- osst device file names fix
  * lsscsi-0.06
* Sat Jan 18 2003 - dgilbert@interlog.com
- output st and osst device file names (rather than "-")
  * lsscsi-0.05
* Thu Jan 14 2003 - dgilbert@interlog.com
- fix multiple listings of st devices (needed for lk 2.5.57)
  * lsscsi-0.04
* Thu Jan 09 2003 - dgilbert@interlog.com
- add --generic option (list sg devices), scsi_level output
  * lsscsi-0.03
* Wed Dec 18 2002 - dgilbert@interlog.com
- add more options including classic mode
  * lsscsi-0.02
* Fri Dec 13 2002 - dgilbert@interlog.com
- original
  * lsscsi-0.01
