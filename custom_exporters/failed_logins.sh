#!/bin/bash
fail_count=$(grep "Failed password" /var/log/auth.log | wc -l)
echo "# HELP failed_ssh_logins Total failed SSH login attempts"
echo "# TYPE failed_ssh_logins gauge"
echo "failed_ssh_logins $fail_count"
