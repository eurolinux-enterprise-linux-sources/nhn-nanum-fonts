%global fontname nhn-nanum
%global fontconf 65-0-%{fontname}

%global common_version 3.020
%global common_desc \
Nanum fonts are collection of commonly-used Myeongjo and Gothic Korean \
font families, designed by Sandoll Communication and Fontrix. The \
publisher is NHN Corporation.


Name:		%{fontname}-fonts
Version:	3.020
Release:	9%{?dist}
Summary:	Nanum family of Korean TrueType fonts

Group:		User Interface/X
License:	OFL
URL:		http://hangeul.naver.com/share.nhn
Source0:	http://cdn.naver.com/naver/NanumFont/fontfiles/NanumFont_TTF_ALL.zip
Source1:	%{name}-brush-fontconfig.conf
Source2:	%{name}-gothic-fontconfig.conf
Source3:	%{name}-myeongjo-fontconfig.conf
Source4:	%{name}-pen-fontconfig.conf
# License text was taken from the upstream web on Nov 21 2012:
# http://help.naver.com/ops/step2/faq.nhn?faqId=15879
Source5:	%{name}-license.txt

BuildArch:	noarch
BuildRequires:	fontpackages-devel

%description
%common_desc


%package common
Summary:   Common files of %{name}
Group:	   User Interface/X
Requires:  fontpackages-filesystem

%description common
%common_desc

This package consists of files used by other %{name} packages.


%package -n %{fontname}-brush-fonts
Version:	1.100
Summary:	Nanum fonts Brush font faces
Requires:	%{name}-common = %{common_version}-%{release}

%description -n %{fontname}-brush-fonts
%common_desc

This package consists of the Nanum fonts Brush font faces.

%_font_pkg -n brush -f %{fontconf}-brush.conf NanumBrush.ttf


%package -n %{fontname}-gothic-fonts
Summary:	Nanum fonts Gothic font faces
Requires:	%{name}-common = %{common_version}-%{release}

%description -n %{fontname}-gothic-fonts
%common_desc

This package consists of the Nanum fonts Gothic font faces.

%_font_pkg -n gothic -f %{fontconf}-gothic.conf NanumGothic.ttf NanumGothicBold.ttf NanumGothicExtraBold.ttf


%package -n %{fontname}-myeongjo-fonts
Summary:	Nanum fonts Myeongjo font faces
Requires:	%{name}-common = %{common_version}-%{release}

%description -n %{fontname}-myeongjo-fonts
%common_desc

This package consists of the Nanum fonts Myeongjo font faces.

%_font_pkg -n myeongjo -f %{fontconf}-myeongjo.conf NanumMyeongjo.ttf NanumMyeongjoBold.ttf NanumMyeongjoExtraBold.ttf


%package -n %{fontname}-pen-fonts
Version:	1.100
Summary:	Nanum fonts Pen font faces
Requires:	%{name}-common = %{common_version}-%{release}

%description -n %{fontname}-pen-fonts
%common_desc

This package consists of the Nanum fonts Pen font faces.

%_font_pkg -n pen -f %{fontconf}-pen.conf NanumPen.ttf


%prep
%setup -q -c
cp -p %{SOURCE5} COPYING


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-brush.conf
install -m 0644 -p %{SOURCE2} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-gothic.conf
install -m 0644 -p %{SOURCE3} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-myeongjo.conf
install -m 0644 -p %{SOURCE4} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-pen.conf

for fconf in %{fontconf}-brush.conf \
    %{fontconf}-gothic.conf \
    %{fontconf}-myeongjo.conf \
    %{fontconf}-pen.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
     %{buildroot}%{_fontconfig_confdir}/$fconf
done


%files common
%doc COPYING


%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 3.020-9
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.020-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 26 2012 Daiki Ueno <dueno@redhat.com> - 3.020-7
- fix broken deps

* Thu Nov 22 2012 Daiki Ueno <dueno@redhat.com> - 3.020-6
- cleanup spec file

* Wed Nov 21 2012 Daiki Ueno <dueno@redhat.com> - 3.020-5
- include license file

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.020-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul  4 2012 Daiki Ueno <dueno@redhat.com> - 3.020-3
- simplify the last change

* Wed Jul  4 2012 Daiki Ueno <dueno@redhat.com> - 3.020-2
- fix <test> usage in fontconfig files (Closes: #837521)

* Mon Feb  6 2012 Daiki Ueno <dueno@redhat.com> - 3.020-1
- new upstream release
- update the priority
  nhn-nanum-fonts -> 65-0, un-core-fonts -> 65-1, baekmuk-ttf-fonts -> 65-2

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.010-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Mar 30 2011 Daiki Ueno <dueno@redhat.com> - 3.010-1
- initial packaging for Fedora

