task :default => [:rebuild]

desc 'Remove old _site and rebuild'
task :rebuild do
  sh 'rm -rf _site'
  sh 'time jekyll build'
end

desc 'Deploy to the live server'
task :deploy => [:rebuild] do
  sh 'rsync -rtzO --delete _site/ emrg@emrg.be:/www/emrg.be/public_html/'
end

desc 'Run Jekyll in server mode'
task :server do
  sh 'jekyll -w serve'
end
