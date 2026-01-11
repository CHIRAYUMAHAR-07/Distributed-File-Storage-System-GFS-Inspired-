# Distributed File Storage System (GFS-Inspired)
Designed a distributed file system with file chunking and replication across multiple nodes. Implemented heartbeat-based failure detection and automated re-replication, recovering from node failures in under 5 seconds.

<img width="1024" height="1024" alt="Gemini_Generated_Image_gjseobgjseobgjse" src="https://github.com/user-attachments/assets/a69e6e9d-9a32-410d-b234-263b4885bfd4" />

# 🎯 Overview
This project implements a distributed file storage system inspired by Google's seminal GFS (Google File System) paper, designed to handle large-scale data storage with high availability, fault tolerance, and automatic recovery capabilities. The system addresses the fundamental challenges of distributed storage: data consistency, replication management, failure detection, and seamless recovery without service interruption.
# Problem Statement
Modern distributed applications require storage systems that can:

Scale horizontally to accommodate growing data volumes without downtime
Survive hardware failures without data loss or extended unavailability
Maintain data consistency across multiple replicas in geographically distributed nodes
Recover automatically from node failures without manual intervention
Provide high throughput for concurrent read and write operations

Traditional centralized storage systems fail under these requirements, creating single points of failure and scalability bottlenecks. This implementation solves these challenges through distributed architecture, intelligent replication strategies, and autonomous failure recovery mechanisms.
# Solution Approach
The system employs a master-worker architecture where a metadata service maintains file system namespace and coordinates chunk placement, while multiple storage nodes handle actual data persistence. Files are divided into fixed-size chunks (64MB by default) distributed across storage nodes with configurable replication factor (default: 3 replicas). A heartbeat-based failure detection system continuously monitors node health, triggering automatic re-replication when failures are detected, achieving sub-5-second recovery times.
# Project Scope
This implementation demonstrates production-level distributed systems engineering including:

Distributed consensus for metadata consistency
Network programming with efficient RPC mechanisms
Concurrent programming handling multiple client requests simultaneously
Failure recovery with automated detection and healing
Data integrity through checksumming and verification
Performance optimization for high-throughput operations

The system is containerized using Docker for easy deployment, includes comprehensive testing infrastructure, and provides monitoring capabilities for observability in production environments.

# 🏗️ System Architecture
High-Level Architecture
The system follows a master-worker topology inspired by GFS, separating metadata management from data storage to optimize for different access patterns and scaling characteristics.

# Component Responsibilities
Metadata Service (Master Node):

Maintains file system namespace (directory hierarchy, file metadata)
Tracks chunk locations across all storage nodes
Coordinates chunk placement for new file writes
Monitors storage node health through heartbeat protocol
Triggers re-replication when under-replicated chunks are detected
Handles client metadata queries (chunk location lookups)
Manages garbage collection of deleted chunks
Ensures consistency through version numbering

# Storage Nodes (Chunk Servers):

Store file chunks as local files on disk
Send periodic heartbeat messages to metadata service
Serve read requests directly to clients
Execute write operations coordinated by metadata service
Participate in chunk replication to restore redundancy after failures
Verify chunk integrity through checksum validation
Report available storage capacity to metadata service

# Client Library:

Provides file system interface to applications (open, read, write, close)
Communicates with metadata service for file location information
Directly reads data from storage nodes after obtaining chunk locations
Handles write pipeline coordination across replicas
Implements retry logic for transient failures
Caches chunk location information to reduce metadata service load

# Data Flow Patterns
Read Operation Flow:

Client sends read request with filename and byte range to metadata service
Metadata service returns list of chunk handles and replica locations
Client directly contacts nearest storage node holding required chunks
Storage node reads chunk from local disk and streams data to client
Client reconstructs file from received chunks

Write Operation Flow:

Client requests chunk allocation from metadata service
Metadata service selects primary replica and secondary replicas
Client pushes data to all replicas through pipeline
Once all replicas acknowledge data receipt, client sends write commit to primary
Primary assigns serial number, applies write, and forwards to secondaries
Secondaries apply write in same order and acknowledge to primary
Primary responds to client confirming write completion

Failure Detection and Recovery Flow:

Storage node fails to send heartbeat within timeout period
Metadata service marks node as failed
Metadata service scans chunk registry identifying under-replicated chunks
For each under-replicated chunk, metadata service instructs healthy node to replicate from remaining replica
Replication completes and metadata service updates chunk location registry
System returns to fully replicated state, typically within 5 seconds

