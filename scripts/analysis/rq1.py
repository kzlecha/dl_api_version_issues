from datetime import datetime

deprecation = {
    "tensorflow":
        {
             datetime(2020, 11, 2): ["tensorflow::tstring/TF_TStrings", "tf.data.experimental.service.DispatchServer", "tf.data.experimental.service.WorkerServer", "tf.distribute.Strategy.experimental_make_numpy_dataset", "experimental_hints", "tf.keras.mixed_precision.experimental"],
             datetime(2020, 7, 27): ["foldr", "foldl", "import_graph_def", "map_fn", "scan", "while_loop", "tf.distribute.experimental.TPUStrategy (renamed to tf.distribute.TPUStrategy)"],
             datetime(2020, 5, 6): ["XLA_CPU", "XLA_GPU"],
             datetime(2020, 1, 8): ["Operation.traceback_with_start_lines", "tf.config.experimentalVirtualDeviceConfiguration", "tf.config.experimental_list_devices"],
             datetime(2019, 9, 30): ["tf.contrib", "tf.contrib.timeseries", "Estimator.export_savedmodel", "tf.feature_column.input_layer", "tf.keras.experimental.export_saved_model", "tf.keras.experimental.function", "lite.OpHint", "lite.experimental", "lite.constant", "tf.string_split", "UnifiedGRU", "CUDNN_INSTALL_PATH", "TENSORRT_INSTALL_PATH", "NCCL_INSTALL_PATH", "NCCL_HDR_PATH"]
        },
    "keras":
        {
            # datetime(2020, 6, 17): ["keras"],
            datetime(2019, 9, 17): ["batch_size", "write_grads", "embeddings_freq", "embeddings_layer_names", "embeddings_metadata", "embeddings_data"],
            datetime(2019, 9, 17): ["batch_size", "write_grads", "embeddings_freq", "embeddings_layer_names", "embeddings_metadata", "embeddings_data"],
            datetime(2018, 6, 6): ["Merge"],
            datetime(2017, 5, 4): ["objectives", "matthews_correlation", "precision", "recall", "fbeta_score", "fmeasure", "MaxoutDense", "Highway", "TimedistributedDense", "dim_ordering", "AtrousConvolution", "Deconvolution2D", "set_image_ordering", "image_ordering", "W_regularizer", "b_regularizer", "b_regularizer", "dropout_W", "dropout_U", "consume_less", "samples_per_epoch", "nb_val_samples", "val_samples"]
        },
    "tesseract":
        {
            datetime(2019, 12, 26): ["cppan"],
            datetime(2019, 7, 7): ["OpenMP"],
            datetime(2018, 10, 29): ["GenericVector::dot_product", "GenericVector::compact", "classify/cutoffs.h", "SavePixForCrash", "IntSimMatrix"],
            datetime(2011, 10, 21): ["ETEXT_STRUCT", "PBLOB", "AccuracyVSpeed"],
            datetime(2016, 1, 1): ["tess4j"]
        },
    "pytorch":
        {
            datetime(2020, 10, 26): ["torch.fft function", "torch.norm", "torch.split", "torch.chunk", "nn.BCELoss", "torch.functional.norm", "ProcessGroup"],
            datetime(2020, 7, 28): ["torch.div", "torch.addcdiv", "recompute_scale_factor", "torch.save"],
            datetime(2020, 4, 21): ["torch.autograd.Function", "BatchNorm", "FeatureDropout", "modules_ordered_dict", "Nonlinearity", "FanMode", "torch.div", "torch.addcdiv", "torch.full", "modules.conv._ConvTransposeMixin", "Tensor.type()"],
            datetime(2020, 1, 15): ["modules_ordered_dict", "Python 2", "Scheduler.step", "C++ 11", "Tensor::is_variable", "torch.jit.quantized"],
            datetime(2019, 10, 10): ["torch.gels:"],
            datetime(2019, 8, 8): ["torch.gels:", "torch.uint8", "autograd.Function", "torch.gels"],
            datetime(2019, 4, 30): ["torch.potrs", "torch.pstrf", "torch.potri", "torch.btrifact_with_info","torch.btrifact", "torch.gesv", "torch.trtrs", "torch.btriunpack", "torch.btrisolve", "IntList", "variable_tensor_functions"],
            datetime(2018, 12, 7): ["torch.utils.trainer", "torch/torch.h", "torch::set_requires_grad", "torch::requires_grad", "torch::getVariableType", "torch.nn.parallel.DistributedDataParallel"],
            datetime(2018, 4, 24): ["volatile", "Tensor.resize", "Tensor.resize_as", "torch.nn.init."],
            datetime(2017, 12, 4): ["Variable.reinforce"],
            datetime(2017, 8, 28): ["masked_copy_"]
        },
    "theano":
        {
            datetime(2017, 9, 7): ["conv2d", "nose-parameterized", "cublas.lib", "cuda.enabled", "enable_initial_driver_test", "gpuarray.sync", "home", "lib.cnmem", "nvcc.", "pycuda.init", "grad", "softmax", "logsoftmax"],
            datetime(2017, 3, 20): ["nose-parameterized", "cublas.lib", "cuda.enabled", "enable_initial_driver_test", "gpuarray.sync", "home", "lib.cnmem", "nvcc.", "pycuda.init", "conv2D", "conv3D", "softmax", "logsoftmax"],
            datetime(2016, 3, 21): ["Param"],
            datetime(2013, 2, 14): ["ProfileMode", "theano.misc.strutil.renderString"],
            datetime(2012, 10, 1): ["Module", "Env"],
            datetime(2012, 2, 23): ["sharedvar.value", "FAST_RUN_NOGC", "STABILIZE", "tensor.shared"],
            datetime(2011, 8, 12): ["FAST_RUN_NOGC", "STABILIZE", "return_steps"],
            datetime(2011, 6, 13): ["tag.shape", "CudaNdarray_new_null", "sandbox/compile", "incsubtensor", "setsubtensor"]
        },
    "caffe":
        {
            datetime(2018, 5, 2): ["caffe2"],
            datetime(2014, 8, 8): ["train_net", "finetune_net", "test_net", "device_query", "net_speed_benchmark"],
            datetime(2014, 5, 20): ["V0"],
            datetime(2014, 3, 18): ["padding layers"]
        },
    "pyspark":
        {
            datetime(2020, 9, 8): ["SQLImplicits.newBooleanSeqEncoder", "SQLImplicits.newByteSeqEncoder", "SQLImplicits.newDoubleSeqEncoder", "SQLImplicits.newFloatSeqEncoder", "SQLImplicits.newIntSeqEncoder", "SQLImplicits.newLongSeqEncoder", "SQLImplicits.newProductSeqEncoder", "SQLImplicits.newShortSeqEncoder", "SQLImplicits.newStringSeqEncoder", "UDFRegistration.register"],
            datetime(2020, 6, 18): ["sql.expressions.javalang.typed", "sql.expressions.scalalang.typed", "UserDefinedAggregateFunction", "BisectingKMeansModel.computeCost", "StringIndexerModel.labels", "SparkConf.setAll(Traversable<Tuple2<String, String>>)", "sql.functions.udf"],
            datetime(2017, 7, 11): ["SQLContext.createExternalTable", "sql.DataFrameReader.json"],
            datetime(2016, 12, 28): ["sql.functions.approxCountDistinct", "sql.functions.toDegrees", "sql.functions.toRadians"],
            datetime(2016, 7, 26): ["HiveContext", "SQLContext", "SQLContext.clearActive", "sql.Dataset.explode", "SQLContext.getOrCreate", "sql.functions.monotonicallyIncreasingId", "sql.Dataset.registerTempTable", "sql.SQLContext.setActive"],
            datetime(2015, 6, 11): ["SQLContext.jdbc", "SQLContext.jsonFile", "SQLContext.jsonRDD", "SQLContext.load", "SQLContext.parquetFile"],
            datetime(2015, 3, 15): ["SQLContext.applySchema"]
        }
               }


for library in deprecation.keys():
    print("\n", library.upper())

    total_dep = 0
    num_releases = 0
    for release_date in deprecation[library].keys():
        total_dep += len(deprecation[library][release_date])
        num_releases += 1

    avg_deprecations = total_dep/num_releases
    print(avg_deprecations)
