#!/usr/bin/env python3
from dataclasses import dataclass
from math import ceil
import argparse
import hashlib
import sys

@dataclass
class Arguments(argparse.Namespace):
  file: str
  numbilets: int
  parameter: int

def parse_args() -> Arguments:
  parser = argparse.ArgumentParser(
    description="Deterministic exam question variant generator",
    epilog="By @renbou",
  )

  parser.add_argument("--file", required=True)
  parser.add_argument("--numbilets", type=int, required=True)
  parser.add_argument("--parameter", type=int, required=True)

  return Arguments(**vars(parser.parse_args()))

def fail(s):
  print(s)
  sys.exit(1)

def generate(s: str, p: int, n: int) -> int:
  # Mapping from Z to N
  if p < 0:
    p = -p * 2
  else:
    p = p * 2 + 1

  h = hashlib.sha256()
  h.update(p.to_bytes(length=ceil(p.bit_length()/8), byteorder="big"))
  h.update(s.encode())
  return int.from_bytes(h.digest(), byteorder="big") % n + 1

def main():
  args = parse_args()

  try:
    with open(args.file, "r") as f:
      students = list(map(str.strip, f.readlines()))
  except FileNotFoundError:
    fail(f"File {args.file} not found.")

  variants = map(lambda s: generate(s, args.parameter, args.numbilets), students)
  for s, v in zip(students, variants):
    print(f"{s}: {v}")

if __name__ == '__main__':
  main()