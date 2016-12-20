#!/bin/sh
/usr/local/bin/dccproc -QCw whiteclnt \
	-a 127.0.0.1 -f postmaster@example.com <<EOF
Message-ID: <1234@example.com>

text
EOF
