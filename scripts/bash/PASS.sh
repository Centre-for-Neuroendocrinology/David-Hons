#!/bin/bash

grep -vP "^#.*PASS\t" '6767SomaticAnnotated (1).vcf' > 6767SomaticAnnotatedPASS.vcf
