import sys
from feature.feature_space import *

def main():

  f = open("/Users/ece/0xdata/h2o-3/h2o-test-feature/featureTestCases.csv", "wb")
  f.write('~'.join(["id", "feature", "feature_params", "data_set_ids", "validation_method", "validation_data_set_id",
                    "description"]) + '\n')

  CosFeatureArgSpace().sample().make_R_tests(f)
  ACosFeatureArgSpace().sample().make_R_tests(f)
  ACoshFeatureArgSpace().sample().make_R_tests(f)
  CoshFeatureArgSpace().sample().make_R_tests(f)
  SinFeatureArgSpace().sample().make_R_tests(f)
  SinhFeatureArgSpace().sample().make_R_tests(f)
  ASinFeatureArgSpace().sample().make_R_tests(f)
  ASinhFeatureArgSpace().sample().make_R_tests(f)
  TanFeatureArgSpace().sample().make_R_tests(f)
  TanhFeatureArgSpace().sample().make_R_tests(f)
  ATanFeatureArgSpace().sample().make_R_tests(f)
  ATanhFeatureArgSpace().sample().make_R_tests(f)
  GammaFeatureArgSpace().sample().make_R_tests(f)
  DigammaFeatureArgSpace().sample().make_R_tests(f)
  TrigammaFeatureArgSpace().sample().make_R_tests(f)
  AbsFeatureArgSpace().sample().make_R_tests(f)
  CeilingFeatureArgSpace().sample().make_R_tests(f)
  FloorFeatureArgSpace().sample().make_R_tests(f)
  ExpFeatureArgSpace().sample().make_R_tests(f)
  Expm1FeatureArgSpace().sample().make_R_tests(f)
  TruncFeatureArgSpace().sample().make_R_tests(f)
  IsCharFeatureArgSpace().sample().make_R_tests(f)
  IsNaFeatureArgSpace().sample().make_R_tests(f)
  IsNumericFeatureArgSpace().sample().make_R_tests(f)
  Log10FeatureArgSpace().sample().make_R_tests(f)
  Log1pFeatureArgSpace().sample().make_R_tests(f)
  Log2FeatureArgSpace().sample().make_R_tests(f)
  LogFeatureArgSpace().sample().make_R_tests(f)
  LGammaFeatureArgSpace().sample().make_R_tests(f)
  LevelsFeatureArgSpace().sample().make_R_tests(f)
  NLevelsFeatureArgSpace().sample().make_R_tests(f)
  NcolFeatureArgSpace().sample().make_R_tests(f)
  NrowFeatureArgSpace().sample().make_R_tests(f)
  NotFeatureArgSpace().sample().make_R_tests(f)
  SignFeatureArgSpace().sample().make_R_tests(f)
  SqrtFeatureArgSpace().sample().make_R_tests(f)
  RoundFeatureArgSpace().sample().make_R_tests(f)
  SignifFeatureArgSpace().sample().make_R_tests(f)
  AndFeatureArgSpace().sample().make_R_tests(f)
  OrFeatureArgSpace().sample().make_R_tests(f)
  DivFeatureArgSpace().sample().make_R_tests(f)
  ModFeatureArgSpace().sample().make_R_tests(f)
  MultFeatureArgSpace().sample().make_R_tests(f)
  SubtFeatureArgSpace().sample().make_R_tests(f)
  IntDivFeatureArgSpace().sample().make_R_tests(f)
  ScaleFeatureArgSpace().sample().make_R_tests(f)
  PowFeatureArgSpace().sample().make_R_tests(f)
  PlusFeatureArgSpace().sample().make_R_tests(f)
  GEFeatureArgSpace().sample().make_R_tests(f)
  GTFeatureArgSpace().sample().make_R_tests(f)
  LEFeatureArgSpace().sample().make_R_tests(f)
  LTFeatureArgSpace().sample().make_R_tests(f)
  EQFeatureArgSpace().sample().make_R_tests(f)
  NEFeatureArgSpace().sample().make_R_tests(f)
  AllFeatureArgSpace().sample().make_R_tests(f)
  CbindFeatureArgSpace().sample().make_R_tests(f)
  ColnamesFeatureArgSpace().sample().make_R_tests(f)
  SliceFeatureArgSpace().sample().make_R_tests(f)
  TableFeatureArgSpace().sample().make_R_tests(f)
  TableFeatureArgSpace(two_col=True).sample().make_R_tests(f)
  QuantileFeatureArgSpace().sample().make_R_tests(f)
  CutFeatureArgSpace().sample().make_R_tests(f)
  MatchFeatureArgSpace().sample().make_R_tests(f)
  WhichFeatureArgSpace().sample().make_R_tests(f)
  RepLenFeatureArgSpace().sample().make_R_tests(f)
  StrSplitFeatureArgSpace().sample().make_R_tests(f)
  ToUpperFeatureArgSpace().sample().make_R_tests(f)
  TransposeFeatureArgSpace().sample().make_R_tests(f)
  MMFeatureArgSpace().sample().make_R_tests(f)
  VarFeatureArgSpace().sample().make_R_tests(f)
  VarFeatureArgSpace(na=False).sample().make_R_tests(f)

  f.close()

if __name__ == "__main__":
  main()