Name:		apache-parent
Version:	35
Release:	1
Summary:	Apache Software Foundation parent POM
Group:		Development/Java
License:	ASL 2.0
URL:		https://maven.apache.org/pom/asf/
Source0:	https://github.com/apache/maven-apache-parent/archive/refs/tags/apache-%{version}.tar.gz
BuildArch:	noarch
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	python
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildSystem:	maven
# The tag is a reactor with a docs module. This package publishes the parent POM only.
BuildOption:	-N validate

%description
Parent POM for Apache Software Foundation projects. Packaged jars inherit
plugin and compiler defaults from this file.

%prep
%setup -q -n maven-apache-parent-apache-%{version}
# Leaving <modules> makes install publish the docs module from this tree.
python - <<'PY'
import re
from pathlib import Path
path = Path("pom.xml")
text = path.read_text()
text = re.sub(r"\n  <modules>.*?</modules>", "", text, count=1, flags=re.S)
path.write_text(text)
PY

%files -f .mfiles
%doc README.md
