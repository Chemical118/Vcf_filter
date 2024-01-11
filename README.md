# VCF_filter

Low memory VCF counter for variant with Python.

## Usage

`vcf_filter.py` filter variant with maximum ALT size and maximum difference length between ALT and REF.

`vcf_loc` : vcf file location

`-d`, `--diff_len_range` : maximum difference length range between ALT and REF

`-a`, `--max_alt_len_range` : maximum ALT size range

You can set range as  `(min value):(max value)`, however if you don't set `min_value` or `max_value` that value will be unlimited.

## Example

- Find SV (structural variant)

  ```bash
  $ python vcf_filter.py example.vcf -d 50:
  ```
- Find SNP

  ```bash
  $ python vcf_filter.py example.vcf -d 1:1 -a :1
  ```
