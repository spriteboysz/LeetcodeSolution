create database if not exists P3475;
use P3475;

CREATE TABLE if not exists Samples (
    sample_id INT,
    dna_sequence VARCHAR(255),
    species VARCHAR(100)
);
Truncate table Samples;
insert into Samples (sample_id, dna_sequence, species)
values ('1', 'ATGCTAGCTAGCTAA', 'Human');
insert into Samples (sample_id, dna_sequence, species)
values ('2', 'GGGTCAATCATC', 'Human');
insert into Samples (sample_id, dna_sequence, species)
values ('3', 'ATATATCGTAGCTA', 'Human');
insert into Samples (sample_id, dna_sequence, species)
values ('4', 'ATGGGGTCATCATAA', 'Mouse');
insert into Samples (sample_id, dna_sequence, species)
values ('5', 'TCAGTCAGTCAG', 'Mouse');
insert into Samples (sample_id, dna_sequence, species)
values ('6', 'ATATCGCGCTAG', 'Zebrafish');
insert into Samples (sample_id, dna_sequence, species)
values ('7', 'CGTATGCGTCGTA', 'Zebrafish');

select sample_id, if((dna_sequence like ('ATG%')), 1, 0) has_start
from Samples;

select sample_id,
    if((dna_sequence like ('%TAA') or dna_sequence like ('%TAG') or dna_sequence like ('%TGA')), 1, 0) has_stop
from Samples;

select s.sample_id, s.dna_sequence, s.species, t1.has_start, t1.has_stop, t1.has_atat, t1.has_ggg
from Samples s
         join (select sample_id, if((dna_sequence like ('ATG%')), 1, 0) has_start,
                   if((dna_sequence like ('%TAA') or dna_sequence like ('%TAG') or dna_sequence like ('%TGA')), 1,
                      0) has_stop, if((dna_sequence like ('%ATAT%')), 1, 0) has_atat,
                   if((dna_sequence like ('%GGG%')), 1, 0) has_ggg
               from Samples) t1 on s.sample_id = t1.sample_id
order by s.sample_id;
