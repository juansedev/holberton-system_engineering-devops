# Equivalent resources:

exec { 'pkill':
    path    => '/usr/bin',
    command => 'pkill -f ./killmenow'
}
