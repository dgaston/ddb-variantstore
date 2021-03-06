from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model


class SampleCoverage(Model):
    __keyspace__ = 'mendelian_coveragestore'
    family = columns.Text(primary_key=True, partition_key=True)
    sample = columns.Text(primary_key=True)

    region = columns.Text(primary_key=True)
    run_id = columns.Text(primary_key=True)
    library_name = columns.Text(primary_key=True)
    program_name = columns.Text(primary_key=True)

    num_libraries_in_run = columns.Integer()
    sequencer_id = columns.Text()
    extraction = columns.Text()
    panel = columns.Text()
    target_pool = columns.Text()

    num_reads = columns.Integer()
    mean_coverage = columns.Float()
    thresholds = columns.List(columns.Integer)
    perc_bp_cov_at_thresholds = columns.Map(columns.Integer, columns.Float)


class RegionCoverage(Model):
    __keyspace__ = 'mendelian_coveragestore'
    region = columns.Text(primary_key=True, partition_key=True)

    family = columns.Text(primary_key=True)
    sample = columns.Text(primary_key=True)
    run_id = columns.Text(primary_key=True)
    library_name = columns.Text(primary_key=True)
    program_name = columns.Text(primary_key=True)

    num_libraries_in_run = columns.Integer()
    sequencer_id = columns.Text()
    extraction = columns.Text()
    panel = columns.Text()
    target_pool = columns.Text()

    num_reads = columns.Integer()
    mean_coverage = columns.Float()
    thresholds = columns.List(columns.Integer)
    perc_bp_cov_at_thresholds = columns.Map(columns.Integer, columns.Float)
