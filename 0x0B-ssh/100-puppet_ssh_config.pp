#!/usr/bin/env bash

# using Puppet to make changes to our configuration file to authenticate without password

# express file type
file { '/etc/ssh/ssh_config':
        # verify file exists
        ensure => present,
}

file_line { 'disable password auth':
        # specify file path
        path => '/etc/ssh/ssh_config',
        # lines to modify in the file
        line => 'PasswordAuthentication no',
        #define a regular expression to match the existing line  before modifications
        match => '^#PasswordAuthentication',
}

file_line { 'Declare identity file':
        # # specifies the path to the file being modified.
        path => '/etc/ssh/ssh_config',
        # defines the line to be modified
        line => 'Identify ~/.ssh/school',
        # specifies a regular expression to match the existing line before modifying it
        match => '^#IdentityFile',
}
