Name:           apache-parent
Version:        10
Release:        14%{?dist}
Summary:        Parent pom file for Apache projects

License:        ASL 2.0
URL:            http://apache.org/
Source0:        http://svn.apache.org/repos/asf/maven/pom/tags/apache-10/pom.xml
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  jpackage-utils
BuildRequires:  apache-resource-bundles
BuildRequires:  maven-remote-resources-plugin

Requires:       apache-resource-bundles

%description
This package contains the parent pom file for apache projects.


%prep
%setup -n %{name}-%{version} -Tc

# This simplifies work with child projects that can use generics
cp %{SOURCE0} .
sed -i 's:<source>1.4</source>:<source>1.5</source>:' pom.xml
sed -i 's:<target>1.4</target>:<target>1.5</target>:' pom.xml

cp %{SOURCE1} LICENSE

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE
