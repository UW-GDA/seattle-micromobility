
#!/bin/bash

for h in {0..23}; do
  pmset schedule wake "$(date -v+1d +%m/%d/%Y) $h:59:57"
  pmset schedule wake "$(date -v+1d +%m/%d/%Y) $h:29:57"
done

