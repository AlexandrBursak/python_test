/**
 Centralize all documentation urls so
 Docs team doesnt have to dig through code base when updating them.
 */

import { get } from 'lodash';
import constants from 'js/constants/client-config';
import { getSessionStorage } from 'js/utility/storage';
import { LANGUAGE_CODES, getCurrentLanguage } from 'js/_core/i18n/i18n';

// All docs are served from `/docs/` but users will see different "books"
// of documentation depending on cluster settings and user permissions.
// - Keep this in-sync with `DataRobot/common/utilities/user_docs.py`
const DOCBOOKS = {
  HTML: 'html',
  ENT_HTML: 'enterprise-html',
};

function getLinkForCurrentDocBook(defaultLink = null, mkdocsLink = null) {
  const isEnglish = getCurrentLanguage() === LANGUAGE_CODES.ENGLISH;
  const isJapanese = getCurrentLanguage() === LANGUAGE_CODES.JAPANESE;
  const shouldUseMkDocsLink = (isEnglish || isJapanese) && mkdocsLink;
  const link = shouldUseMkDocsLink ? mkdocsLink : defaultLink;

  if (link === null || typeof link === 'string') {
    return link;
  }

  const defaultServerBook = get(
    constants,
    'docs_config.book_folder',
    DOCBOOKS.HTML
  );
  const defaultUserBook = get(
    getSessionStorage('docs_config'),
    'book_folder',
    null
  );

  return link[defaultUserBook || defaultServerBook];
}

// All documentation links below must provide a url for each book.
// This also applies for links that are specific to enterprise installs and not cloud.

const aiCatalog = {
  get overview() {
    return getLinkForCurrentDocBook(
      {
        [DOCBOOKS.HTML]: 'load/ai-catalog/index.html',
        [DOCBOOKS.ENT_HTML]: 'load/ai-catalog/index.html',
      },
      {
        [DOCBOOKS.HTML]: 'data/import-data/catalog.html',
        [DOCBOOKS.ENT_HTML]: 'data/import-data/catalog.html',
      }
    );
  },
  get catalog() {
    return getLinkForCurrentDocBook(
      {
        [DOCBOOKS.HTML]: 'load/ai-catalog/catalog.html',
        [DOCBOOKS.ENT_HTML]: 'load/ai-catalog/catalog.html',
      },
      {
        [DOCBOOKS.HTML]: 'data/import-data/catalog.html',
        [DOCBOOKS.ENT_HTML]: 'data/import-data/catalog.html',
      }
    );
  },
  get catalogAsset() {
    return getLinkForCurrentDocBook(
      {
        [DOCBOOKS.HTML]: 'load/ai-catalog/catalog-asset.html',
        [DOCBOOKS.ENT_HTML]: 'load/ai-catalog/catalog-asset.html',
      },
      {
        [DOCBOOKS.HTML]: 'data/import-data/catalog-asset.html',
        [DOCBOOKS.ENT_HTML]: 'data/import-data/catalog-asset.html',
      }
    );
  },
  get catalogAssetData() {
    return getLinkForCurrentDocBook(
      {
        [DOCBOOKS.HTML]: 'load/ai-catalog/catalog-asset.html#prof-info',
        [DOCBOOKS.ENT_HTML]: 'load/ai-catalog/catalog-asset.html#prof-info',
      },
      {
        [DOCBOOKS.HTML]: 'data/import-data/catalog-asset.html#view-asset-data',
        [DOCBOOKS.ENT_HTML]:
          'data/import-data/catalog-asset.html#view-asset-data',
      }
    );
  },
  get catalogAssetFeatureLists() {
    return getLinkForCurrentDocBook(
      {
        [DOCBOOKS.HTML]: 'load/ai-catalog/catalog-asset.html#flists',
        [DOCBOOKS.ENT_HTML]: 'load/ai-catalog/catalog-asset.html#flists',
      },
      {
        [DOCBOOKS.HTML]:
          'data/import-data/catalog-asset.html#work-with-feature-lists',
        [DOCBOOKS.ENT_HTML]:
          'data/import-data/catalog-asset.html#work-with-feature-lists',
      }
    );
  },
  get catalogAssetRelationships() {
    return getLinkForCurrentDocBook(
      {
        [DOCBOOKS.HTML]: 'load/ai-catalog/catalog-asset.html#safer',
        [DOCBOOKS.ENT_HTML]: 'load/ai-catalog/catalog-asset.html#safer',
      },
      {
        [DOCBOOKS.HTML]:
          'data/import-data/catalog-asset.html#view-configured-relationships',
        [DOCBOOKS.ENT_HTML]:
          'data/import-data/catalog-asset.html#view-configured-relationships',
      }
    );
  },
  get catalogAssetVersions() {
    return getLinkForCurrentDocBook(
      {
        [DOCBOOKS.HTML]: 'load/ai-catalog/catalog-asset.html#vers-history',
        [DOCBOOKS.ENT_HTML]: 'load/ai-catalog/catalog-asset.html#vers-history',
      },
      {
        [DOCBOOKS.HTML]:
          'data/import-data/catalog-asset.html#view-version-history',
        [DOCBOOKS.ENT_HTML]:
          'data/import-data/catalog-asset.html#view-version-history',
      }
    );
  },
  get scheduledSnapshot() {
    return getLinkForCurrentDocBook(
      {
        [DOCBOOKS.HTML]: 'load/ai-catalog/snapshot.html',
        [DOCBOOKS.ENT_HTML]: 'load/ai-catalog/snapshot.html',
      },
      {
        [DOCBOOKS.HTML]: 'data/import-data/snapshot.html',
        [DOCBOOKS.ENT_HTML]: 'data/import-data/snapshot.html',
      }
    );
  },
};

const deployment = {
  get overview() {
    return getLinkForCurrentDocBook(
      {
        [DOCBOOKS.HTML]: 'deploy/index.html',
        [DOCBOOKS.ENT_HTML]: 'predictions/deploy/index.html',
      },
      {
        [DOCBOOKS.HTML]: 'mlops/deployment/index.html',
        [DOCBOOKS.ENT_HTML]: 'mlops/deployment/index.html',
      }
    );
  },
  get inventory() {
    return getLinkForCurrentDocBook(
      {
        [DOCBOOKS.HTML]: 'deploy/inventory.html',
        [DOCBOOKS.ENT_HTML]: 'predictions/deploy/inventory.html',
      },
      {
        [DOCBOOKS.HTML]: 'mlops/manage/deploy-inventory.html',
        [DOCBOOKS.ENT_HTML]: 'mlops/manage/deploy-inventory.html',
      }
    );
  },
  get disableDeploymentMonitoring() {
    return getLinkForCurrentDocBook(
      {
        [DOCBOOKS.HTML]: 'deploy/index.html#disable-dep-monitoring',
        [DOCBOOKS.ENT_HTML]:
          'predictions/deploy/index.html#disable-dep-monitoring',
      },
      {
        [DOCBOOKS.HTML]:
          'mlops/manage/deploy-settings.html#deployments-with-monitoring-disabled',
        [DOCBOOKS.ENT_HTML]:
          'mlops/manage/deploy-settings.html#deployments-with-monitoring-disabled',
      }
    );
  },
  get settings() {
    return getLinkForCurrentDocBook(
      {
        [DOCBOOKS.HTML]: 'deploy/settings.html',
        [DOCBOOKS.ENT_HTML]: 'predictions/deploy/settings.html',
      },
      {
        [DOCBOOKS.HTML]: 'mlops/manage/deploy-settings.html',
        [DOCBOOKS.ENT_HTML]: 'mlops/manage/deploy-settings.html',
      }
    );
  },
  get humility() {
    return getLinkForCurrentDocBook(
      {
        [DOCBOOKS.HTML]: 'deploy/humble.html',
        [DOCBOOKS.ENT_HTML]: 'predictions/deploy/humble.html',
      },
      {
        [DOCBOOKS.HTML]: 'mlops/governance/humble.html',
        [DOCBOOKS.ENT_HTML]: 'mlops/governance/humble.html',
      }
    );
  },
  get predictionWarnings() {
    return getLinkForCurrentDocBook(
      {
        [DOCBOOKS.HTML]: 'deploy/settings.html#prediction-warnings',
        [DOCBOOKS.ENT_HTML]:
          'predictions/deploy/settings.html#prediction-warnings',
      },
      {
        [DOCBOOKS.HTML]:
          'mlops/manage/deploy-settings.html#prediction-warnings',
        [DOCBOOKS.ENT_HTML]:
          'mlops/manage/deploy-settings.html#prediction-warnings',
      }
    );
  },
  get setupAccuracy() {
    return getLinkForCurrentDocBook(
      {
        [DOCBOOKS.HTML]: 'deploy/setup-accuracy.html',
        [DOCBOOKS.ENT_HTML]: 'predictions/deploy/setup-accuracy.html',
      },
      {
        [DOCBOOKS.HTML]: 'mlops/manage/setup-accuracy.html',
        [DOCBOOKS.ENT_HTML]: 'mlops/manage/setup-accuracy.html',
      }
    );
  },
  get associationId() {
    return getLinkForCurrentDocBook(
      {
        [DOCBOOKS.HTML]: 'deploy/setup-accuracy.html#association',
        [DOCBOOKS.ENT_HTML]:
          'predictions/deploy/setup-accuracy.html#association',
      },
      {
        [DOCBOOKS.HTML]: 'mlops/manage/setup-accuracy.html#association-id',
        [DOCBOOKS.ENT_HTML]: 'mlops/manage/setup-accuracy.html#association-id',
      }
    );
  },
};

const predictionEnvironments = {
  get overview() {
    return getLinkForCurrentDocBook(
      {
        [DOCBOOKS.HTML]: 'deploy/pred-env.html',
        [DOCBOOKS.ENT_HTML]: 'deploy/pred-env.html',
      },
      {
        [DOCBOOKS.HTML]: 'mlops/deployment/pred-env.html',
        [DOCBOOKS.ENT_HTML]: 'mlops/deployment/pred-env.html',
      }
    );
  },
};

const compliance = {
  get overview() {
    return getLinkForCurrentDocBook(
      'modeling/investigate/compliance/compliance.html',
      'modeling/analyze-models/compliance/compliance.html'
    );
  },
};

const data = {
  get explore() {
    return getLinkForCurrentDocBook(
      'modeling/build-basic/model-data.html#explore',
      'modeling/build-models/build-basic/model-data.html#exploring-your-data'
    );
  },
  get featureTransform() {
    return getLinkForCurrentDocBook('modeling/curate/feature-transforms.html');
  },
  get createFeatureTransform() {
    return getLinkForCurrentDocBook(
      'modeling/curate/feature-transforms.html#creating-transformations',
      'data/transform-data/transform-primary-datasets/feature-transforms.html'
    );
  },
  get featureVarTypeTransform() {
    return getLinkForCurrentDocBook(
      'docs/modeling/curate/feature-transforms.html#transforming-the-variable-type-for-multiple-features',
      'data/transform-data/transform-primary-datasets/feature-transforms.html#multiple-feature-transformations'
    );
  },
  get featureTransformSyntax() {
    return getLinkForCurrentDocBook(
      'modeling/curate/feature-transforms.html#user-transform-syntax',
      'data/transform-data/transform-primary-datasets/feature-transforms.html#transform-options-and-syntax'
    );
  },
  get importance() {
    return getLinkForCurrentDocBook(
      'modeling/build-basic/model-ref.html#summary-info',
      'modeling/reference/model-detail/model-ref.html#interpreting-data-summary-information'
    );
  },
  get partitioning() {
    return getLinkForCurrentDocBook(
      'reference/data-partitioning.html',
      'modeling/reference/data-detail/data-partitioning.html'
    );
  },
  get eureqaPartitioning() {
    return getLinkForCurrentDocBook(
      'reference/eureqa/advanced-options.html#eur-partition',
      'modeling/reference/eureqa/advanced-options.html#eureqa-data-partitioning'
    );
  },
  get sampleSizeWarning() {
    return getLinkForCurrentDocBook(
      'load/overview-eda.html#eda-details',
      'modeling/reference/model-detail/eda-explained.html'
    );
  },
  get fileTypes() {
    return getLinkForCurrentDocBook(
      'load/file-types.html#spec-column',
      'data/import-data/file-types.html#special-column-detection'
    );
  },
  get targetLeakage() {
    return getLinkForCurrentDocBook(
      'modeling/build-basic/model-ref.html#target-leak',
      'data/analyze-data/data-quality.html#target-leakage'
    );
  },
  get datasetRequirements() {
    return getLinkForCurrentDocBook(
      'load/file-types.html',
      'data/import-data/file-types.html'
    );
  },
  get learningCurves() {
    return getLinkForCurrentDocBook(
      'modeling/compare/other-model-tabs.html#learning-curves',
      'modeling/analyze-models/other/learn-curve.html'
    );
  },
  get speedVAccuracy() {
    return getLinkForCurrentDocBook(
      'modeling/compare/other-model-tabs.html#speed-acc',
      'modeling/analyze-models/other/speed.html'
    );
  },
  get modelCompare() {
    return getLinkForCurrentDocBook(
      'modeling/compare/other-model-tabs.html#model-compare',
      'modeling/analyze-models/other/model-compare.html'
    );
  },
};

const ingest = {
  get overview() {
    return getLinkForCurrentDocBook(
      'load/overview-eda.html',
      'modeling/reference/model-detail/eda-explained.html'
    );
  },
  get jdbc() {
    return getLinkForCurrentDocBook(
      'modeling/load/jdbc.html',
      'data/connect-data-sources/data-conn.html'
    );
  },
};

const project = {
  get manage() {
    return getLinkForCurrentDocBook(
      'modeling/manage/manage-projects.html',
      'modeling/build-models/manage/manage-projects.html'
    );
  },
  get modelingModes() {
    return getLinkForCurrentDocBook(
      'modeling/build-basic/model-data.html#model-modes',
      'modeling/build-models/build-basic/model-data.html#set-the-modeling-mode'
    );
  },
  get share() {
    return getLinkForCurrentDocBook(
      'modeling/manage/manage-projects.html#project-share',
      'modeling/build-models/manage/manage-projects.html#share-a-project'
    );
  },
  get unlockHoldout() {
    return getLinkForCurrentDocBook(
      'modeling/compare/unlocking-holdout.html',
      'modeling/build-models/build-basic/unlocking-holdout.html'
    );
  },
};

const insights = {
  get overview() {
    return getLinkForCurrentDocBook(
      'modeling/compare/analyze-insights.html',
      'modeling/analyze-models/other/analyze-insights.html'
    );
  },
  get wordCloud() {
    return getLinkForCurrentDocBook(
      'modeling/compare/analyze-insights.html#word-cloud',
      'modeling/analyze-models/other/analyze-insights.html#word-cloud-insights'
    );
  },
};

const models = {
  get leaderboard() {
    return getLinkForCurrentDocBook(
      'modeling/compare/leaderboard.html',
      'modeling/reference/model-detail/leaderboard-ref.html'
    );
  },
  get featureImpact() {
    return getLinkForCurrentDocBook(
      'modeling/investigate/understand/feature-impact.html',
      'modeling/analyze-models/understand/feature-impact.html'
    );
  },
  get featureImpactRedundant() {
    return getLinkForCurrentDocBook(
      'modeling/investigate/understand/feature-impact.html#redundant',
      'modeling/analyze-models/understand/feature-impact.html#remove-redundant-features'
    );
  },
  get featureImpactHighCorrelation() {
    return getLinkForCurrentDocBook(
      'modeling/investigate/understand/feature-impact.html#gen-fi',
      'modeling/analyze-models/understand/feature-impact.html#generate-the-feature-impact-chart'
    );
  },
  get featureImpactForAnomalyDetection() {
    return getLinkForCurrentDocBook(
      'modeling/investigate/understand/feature-impact.html#fi-anom',
      'modeling/analyze-models/understand/feature-impact.html#feature-impact-for-unsupervised-projects'
    );
  },
  get liftChart() {
    return getLinkForCurrentDocBook(
      'modeling/investigate/evaluate/lift-chart.html',
      'modeling/analyze-models/evaluate/lift-chart.html'
    );
  },
  get rocCurve() {
    return getLinkForCurrentDocBook(
      'modeling/investigate/evaluate/roc.html',
      'modeling/analyze-models/evaluate/roc-curve-tab/index.html'
    );
  },
  get residuals() {
    return getLinkForCurrentDocBook(
      'modeling/investigate/evaluate/residuals.html',
      'modeling/analyze-models/evaluate/residuals.html'
    );
  },
  get featureFit() {
    return getLinkForCurrentDocBook(
      'modeling/investigate/evaluate/feature-fit.html',
      'modeling/analyze-models/evaluate/feature-fit.html'
    );
  },
  get accuracyOverTime() {
    return getLinkForCurrentDocBook(
      'modeling/investigate/evaluate/aot.html',
      'modeling/analyze-models/evaluate/aot.html'
    );
  },
  get anomalyAssessment() {
    return getLinkForCurrentDocBook(
      'modeling/investigate/evaluate/anom-viz.html',
      'modeling/analyze-models/evaluate/anom-viz.html'
    );
  },
  get accuracyOverSpace() {
    return getLinkForCurrentDocBook(null);
  },
  get spatialEffects() {
    return getLinkForCurrentDocBook(null);
  },
  get seriesInsights() {
    return getLinkForCurrentDocBook(
      'modeling/investigate/evaluate/series-acc.html',
      'modeling/analyze-models/evaluate/series-acc.html'
    );
  },
  get stability() {
    return getLinkForCurrentDocBook(
      'modeling/investigate/evaluate/stability.html',
      'modeling/analyze-models/evaluate/stability.html'
    );
  },
  get forecastingAccuracy() {
    return getLinkForCurrentDocBook(
      'modeling/investigate/evaluate/forecast-acc.html',
      'modeling/analyze-models/evaluate/forecast-acc.html'
    );
  },
  get confusionMatrix() {
    return getLinkForCurrentDocBook(
      'modeling/investigate/evaluate/multiclass.html',
      'modeling/analyze-models/evaluate/multiclass.html'
    );
  },
  get imageAugmentation() {
    return getLinkForCurrentDocBook(
      'modeling/visual-ai/tti-augment/index.html',
      'modeling/special-workflows/visual-ai/tti-augment/index.html'
    );
  },
  get imageAugmentationNewImagesPerOriginal() {
    return getLinkForCurrentDocBook(
      'modeling/visual-ai/tti-augment/ttia-lists.html#image-new',
      'modeling/special-workflows/visual-ai/tti-augment/ttia-lists.html#new-images-per-original'
    );
  },
  get advancedTuning() {
    return getLinkForCurrentDocBook(
      'modeling/investigate/evaluate/adv-tuning.html',
      'modeling/analyze-models/evaluate/adv-tuning.html'
    );
  },
  get featureEffects() {
    return getLinkForCurrentDocBook(
      'modeling/investigate/understand/feature-effects.html',
      'modeling/analyze-models/understand/feature-effects.html'
    );
  },
  get featureEffectsHighCorrelation() {
    return getLinkForCurrentDocBook(
      'modeling/investigate/understand/feature-effects.html#opt-display',
      'modeling/analyze-models/understand/feature-effects.html#display-options'
    );
  },
  // TODO: correct this link after https://datarobot.atlassian.net/browse/DOC-2728
  get clusterInsights() {
    return getLinkForCurrentDocBook(
      'modeling/investigate/understand/cluster-insights.html'
    );
  },
  get predictionExplanations() {
    return getLinkForCurrentDocBook(
      'modeling/investigate/understand/pred-explain/index.html',
      'modeling/analyze-models/understand/pred-explain/index.html'
    );
  },
  get shapPredictionExplanations() {
    return getLinkForCurrentDocBook(
      'modeling/investigate/understand/pred-explain/shap-pe.html',
      'modeling/analyze-models/understand/pred-explain/shap-pe.html'
    );
  },
  get imageEmbeddings() {
    return getLinkForCurrentDocBook(
      'modeling/visual-ai/vai-insights.html#image-bed',
      'modeling/special-workflows/visual-ai/vai-insights.html#image-embeddings'
    );
  },
  get activationMaps() {
    return getLinkForCurrentDocBook(
      'modeling/visual-ai/vai-insights.html#using-activation-maps',
      'modeling/special-workflows/visual-ai/vai-insights.html#activation-maps'
    );
  },
  get neuralNetworkVisualizer() {
    return getLinkForCurrentDocBook(null);
  },
  get blueprint() {
    return getLinkForCurrentDocBook(
      'modeling/investigate/describe/blueprints.html',
      'modeling/analyze-models/describe/blueprints.html'
    );
  },
  get modelInfo() {
    return getLinkForCurrentDocBook(
      'modeling/investigate/describe/model-info.html',
      'modeling/analyze-models/describe/model-info.html'
    );
  },
  get coefficients() {
    return getLinkForCurrentDocBook(
      'modeling/investigate/describe/coefficients.html',
      'modeling/analyze-models/describe/coefficients.html'
    );
  },
  get ratingTable() {
    return getLinkForCurrentDocBook(
      'modeling/investigate/describe/rating-table.html',
      'modeling/analyze-models/describe/rating-table.html'
    );
  },
  get eureqa() {
    return getLinkForCurrentDocBook(
      'modeling/investigate/describe/eureqa.html',
      'modeling/analyze-models/describe/eureqa.html'
    );
  },
  get log() {
    return getLinkForCurrentDocBook(
      'modeling/investigate/describe/log.html',
      'modeling/analyze-models/describe/log.html'
    );
  },
  get dataQualityReport() {
    return getLinkForCurrentDocBook(
      'modeling/investigate/describe/dq-report.html',
      'modeling/analyze-models/describe/dq-report.html'
    );
  },
  get runAdditional() {
    return getLinkForCurrentDocBook(
      'modeling/manage/creating-addl-models.html',
      'modeling/build-models/build-basic/creating-addl-models.html'
    );
  },
  get recommended() {
    return getLinkForCurrentDocBook(
      'modeling/compare/leaderboard.html#rec-badge',
      'modeling/reference/model-detail/model-rec-process.html'
    );
  },
  get shapOnlyMode() {
    return getLinkForCurrentDocBook(
      'modeling/investigate/understand/pred-explain/shap-pe.html',
      'modeling/analyze-models/understand/pred-explain/shap-pe.html'
    );
  },
  get blenders() {
    return getLinkForCurrentDocBook(
      'modeling/compare/leaderboard.html#understanding-blender-models',
      'modeling/reference/model-detail/leaderboard-ref.html#blender-models'
    );
  },
  get monotonic() {
    return getLinkForCurrentDocBook(
      'modeling/investigate/describe/monotonic.html',
      'modeling/analyze-models/describe/monotonic.html'
    );
  },
  get multilabelFeatureProperties() {
    return getLinkForCurrentDocBook(
      'public-preview/automl-preview/multilabel.html#feature-statistics-tab',
      'release/public-preview/automl-preview/multilabel.html#feature-statistics-tab'
    );
  },
  get perLabelMetrics() {
    return getLinkForCurrentDocBook(
      'public-preview/automl-preview/multilabel.html#per-label-metrics',
      'release/public-preview/automl-preview/multilabel.html#per-label-metrics'
    );
  },
  get modelTrainingDashboard() {
    return getLinkForCurrentDocBook(
      'modeling/investigate/evaluate/training-dash.html',
      'modeling/analyze-models/evaluate/training-dash.html'
    );
  },
  get optimizationMetrics() {
    return getLinkForCurrentDocBook(
      'reference/opt-metric.html#optimization-metrics',
      'modeling/reference/model-detail/opt-metric.html'
    );
  },
};

const partners = {
  get index() {
    return getLinkForCurrentDocBook(
      'reference/partners/index.html',
      'modeling/biz-ops/partners/index.html'
    );
  },
};

const predictions = {
  get index() {
    return getLinkForCurrentDocBook('predictions/index.html');
  },
  get apiDocs() {
    return getLinkForCurrentDocBook('predictions/api/dr-predapi.html');
  },
  get batch() {
    return getLinkForCurrentDocBook('predictions/ui/predict.html');
  },
  get codegen() {
    return getLinkForCurrentDocBook(
      'predictions/scoring-code/scorecode.html',
      'predictions/scoring-code/index.html'
    );
  },
  get deploy() {
    return getLinkForCurrentDocBook('predictions/ui/deploy-model.html');
  },
  get download() {
    return getLinkForCurrentDocBook('predictions/ui/download.html');
  },
  get downloadZip() {
    return getLinkForCurrentDocBook(
      'predictions/ui/download.html#download-zip',
      'predictions/ui/download.html#downloading-content'
    );
  },
  get hadoop() {
    return getLinkForCurrentDocBook('predictions/ui/hadoop.html');
  },
  get prime() {
    return getLinkForCurrentDocBook('predictions/ui/prime.html');
  },
  get largePredictions() {
    return getLinkForCurrentDocBook(
      'predictions/batch/batch-prediction-api/large-preds-api.html'
    );
  },
  get cliScripts() {
    return getLinkForCurrentDocBook('predictions/batch/cli-scripts.html');
  },
  get batchPredictionsAPI() {
    return getLinkForCurrentDocBook(
      'predictions/batch/batch-prediction-api/index.html'
    );
  },
};

const queue = {
  get workers() {
    return getLinkForCurrentDocBook(
      'modeling/build-basic/worker-queue.html',
      'modeling/build-models/build-basic/worker-queue.html'
    );
  },
  get gpuWorkers() {
    return getLinkForCurrentDocBook('');
  }, // todo - VIZAI-1394
};

const repository = {
  get overview() {
    return getLinkForCurrentDocBook(
      'modeling/build-adv/repository.html',
      'modeling/build-models/build-basic/repository.html'
    );
  },
  get scaleoutHadoop() {
    return getLinkForCurrentDocBook(
      'modeling/build-adv/repository.html#scaleout-hadoop',
      'modeling/build-models/build-basic/repository.html#scaleout-models'
    );
  },
};

const advancedOptions = {
  get additionalParams() {
    return getLinkForCurrentDocBook(
      'modeling/build-adv/adv-opt-link.html#set-addl-params',
      'modeling/build-models/adv-opt/additional.html'
    );
  },
  get additionalParamsWeighting() {
    return getLinkForCurrentDocBook(
      'modeling/adv-opt/additional.html#using-exoff',
      'modeling/build-models/adv-opt/additional.html#set-exposure'
    );
  },
};

const safer = {
  get sumCat() {
    return getLinkForCurrentDocBook(
      'modeling/curate/histogram.html#summ-cat',
      'data/analyze-data/histogram.html#summarized-categorical-features'
    );
  },
  get featureDiscovery() {
    return getLinkForCurrentDocBook(
      'modeling/feature-discovery/index.html',
      'data/transform-data/feature-discovery/index.html'
    );
  },
  get makingPredictions() {
    return getLinkForCurrentDocBook(
      'public-beta/feg/fd-predict.html',
      'data/transform-data/feature-discovery/fd-predict.html'
    );
  },
  get overview() {
    return getLinkForCurrentDocBook(
      'public-beta/feg/index.html',
      'data/transform-data/feature-discovery/fd-overview.html'
    );
  },
  get snowflakePushDownCompatibility() {
    return getLinkForCurrentDocBook(
      'modeling/feature-discovery/fd-overview.html#snowflake-int',
      'data/transform-data/feature-discovery/fd-overview.html#snowflake-integration'
    );
  },
};

const settings = {
  get gettingHelp() {
    return getLinkForCurrentDocBook(
      'settings/getting-help.html',
      'admin/for-users/getting-help.html'
    );
  },
  get userPermaDelete() {
    return getLinkForCurrentDocBook('release/public-preview/perma-delete.html');
  },
};

const timeSeries = {
  get crossSeries() {
    return getLinkForCurrentDocBook(
      'time/time-series.html#cross-series',
      'modeling/build-models/adv-opt/ts-adv-opt.html#calculate-features-across-series'
    );
  },
  get makePredictionsTab() {
    return getLinkForCurrentDocBook(
      'time/time-series.html#pred-tab',
      'modeling/time/time-series.html#make-predictions-tab'
    );
  },
  get shap() {
    return getLinkForCurrentDocBook(
      'reference/shap.html',
      'modeling/reference/model-detail/shap.html'
    );
  },
  get dnd() {
    return getLinkForCurrentDocBook(
      'modeling/adv-opt/ts-adv-opt.html#dnd',
      'modeling/build-models/adv-opt/ts-adv-opt.html#exclude-features-from-derivation'
    );
  },
  get autopilot() {
    return getLinkForCurrentDocBook(
      'time/multistep-ta.html',
      'modeling/time/multistep-ta.html'
    );
  },
};

const ide = {
  get overview() {
    return getLinkForCurrentDocBook('modeling/build-adv/ides/index.html');
  },
};

const modelRegistry = {
  get customModels() {
    return getLinkForCurrentDocBook(
      'registry/index.html',
      'mlops/deployment/registry/index.html'
    );
  },
};

const customModels = {
  PPS: {
    get documentation() {
      return getLinkForCurrentDocBook(
        'public-beta/custom-pps.html',
        'mlops/deployment/deploy-pred/custom-pps.html'
      );
    },
  },
  get modelTesting() {
    return getLinkForCurrentDocBook(
      'registry/custom-models/custom-inf-model.html#testing-a-custom-inference-model',
      'mlops/deployment/custom-models/custom-inf-model.html#testing-a-custom-inference-model'
    );
  },
};

const applications = {
  get overview() {
    return getLinkForCurrentDocBook(
      'apps/index.html',
      'modeling/biz-ops/apps/index.html'
    );
  },
  get predictor() {
    return getLinkForCurrentDocBook(
      'docs/apps/pred-app.html',
      'modeling/biz-ops/apps/pred-app.html'
    );
  },
  get optimizer() {
    return getLinkForCurrentDocBook(
      'docs/apps/opt-app.html',
      'modeling/biz-ops/apps/opt-app.html'
    );
  },
  get whatIf() {
    return getLinkForCurrentDocBook(
      'docs/apps/what-if-app.html',
      'modeling/biz-ops/apps/what-if-app.html'
    );
  },
};

const biasAndFairness = {
  get index() {
    return getLinkForCurrentDocBook(
      'modeling/adv-opt/fairness-metrics.html',
      'modeling/build-models/adv-opt/fairness-metrics.html'
    );
  },
};

const section = {
  logo: ingest.overview,
  data: data.explore,
  models: models.leaderboard,
  deployments: deployment.inventory,
  modelRegistry: modelRegistry.customModels,
  insights: insights.overview,
  ide: ide.overview,
  repo: repository.overview,
  applications,
  aiCatalog: aiCatalog.overview,
};

export const docLinks = {
  compliance,
  deployment,
  predictionEnvironments,
  section,
  project,
  ide,
  insights,
  models,
  data,
  ingest,
  partners,
  predictions,
  queue,
  repository,
  advancedOptions,
  safer,
  settings,
  timeSeries,
  aiCatalog,
  biasAndFairness,
  customModels,
};
